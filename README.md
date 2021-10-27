# NirCAS
A canteen management system
<br><br>
<h2>About NirCAS</h2>
<p>We have built this project as part of our Innovative assignment for the course 'Application Development Frameworks'. The backend has been built with <a href="https://www.djangoproject.com/">Django</a>. The frontend used has CSS and JavaScript. The name NirCAS has roots in the name of our University as well as describes the aim of the project - <i><b>Nir</b>ma <b>C</b>anteen <b>A</b>utomation <b>S</b>ystem.</i></p>

<h2>Motivation</h2>
<p>The motivation of this project comes from the concept used in our university's canteen. The procedure followed is : 
	<ol>
		<li>Firstly, a customer is required to purchase coupons from the coupon counter in exchange of cash. These coupons do not have the name of the expected food item specified on them, they are just coupons with the required amount mentioned.</li>
		<li>The next step for the customer is to pass this coupon(s) to the designated counters to get the expected food items. The customer is required to verbally specify their required food item to the employee(s) handling the counter.</li>
		<li>After this, the customer is given the food item by the employee who collected their coupon.</li>
	</ol>
	<br>
	What we have worked on in this procedure?
	<ul>
		<li>We have added the functionality of the name of the food item being specified on the coupon to avoid confusion with the employee giving the food item.</li>
		<li>We gave the option to a customer to work through a credit system to avoid issues with cash, like, worrying about the exact change or having to exchange money in times of situations where a disease transmittable via touch like COVID-19.</li>
		<li>we have proposed a 3 level heirarchy in the maintenance of the website with user types like 'Admin', 'Manager', 'Cashier' and 'Customer'. More details have been described <a href="https://github.com/Ishikashah2510/nircas_adf/blob/master/README.md#details-about-the-responsibilities-given-to-different-types-of-users">below</a>.</li>
	</ul>
</p>

<h2>About the models</h2>
<p>A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.</p><br>
<h3>Models in <i>access</i> application</h3>

```Python

class Users(models.Model):
    user_types = [
        ('Customer', 'Customer'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
    birthdate = models.DateField(blank=True, null=True)
    mobile_no = models.IntegerField(unique=True)
    user_type = models.CharField(choices=user_types,
                                 default='Customer',
                                 max_length=9)
				 
```
<br>
The above model, Users is used to store the details of each kind of user. It is a basic model with a choices list for user type<br>
<h3>Models in manager app</h3>

```Python

def validate_existence(value):
    if FoodItems.objects.filter(name__iexact=value).exists():
        raise ValidationError(
            'Sorry, item already exists'
        )


class FoodItems(models.Model):
    category_choices = [
        ('Punjabi', 'Punjabi'),
        ('Chinese', 'Chinese'),
        ('Sandwich', 'Sandwich'),
        ('Fast food', 'Fast food'),
        ('South Indian', 'South Indian'),
        ('Breakfast', 'Breakfast')
    ]

    name = models.CharField(max_length=100, unique=True, validators=[validate_existence])
    cost = models.FloatField()
    description = models.CharField(max_length=160)
    serves = models.IntegerField()
    rating = models.FloatField(default=5)
    category = models.CharField(max_length=100,
                                choices=category_choices,
                                default='Punjabi')
    photo = models.ImageField(upload_to='food/',
                              default='food/default_food.jfif')

    def __str__(self):
        return self.name

```
The above model, FoodItems, is used to store different food items which can be used with CRUD functionality by the manager. There is also a Image Field for the photo of the food.<br><br>

```Python

class EverydayOffers(models.Model):
    discount = models.FloatField()
    food_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE)

```
The above model, EverydayOffers, is used to store the discount for the kind of food item selected. For example, if hot dog is a food item in the FoodItems table, we can store it's discount in this model. This model too supports CRUD functionality for the manager.<br><br>
<h3>Models defined in the Cashier application</h3>

```Python

def unique_key_generator():
    length = random.randint(5, 10)
    secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return secret_code


class Orders(models.Model):
    order_id = models.CharField(max_length=10, unique=True, default=unique_key_generator, auto_created=True)
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    total_cost = models.FloatField(default=0)
    items = models.ManyToManyField(FoodItems, through='ItemQuantity', through_fields=('order_id', 'food_id'))
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id} <-----> {self.total_cost}"

```
The above model, Orders, stores the details of a particular Order, where the order_id is generated randomly using the unique_key_generator() function. The field <i>items</i> is a ManyToMany field to the model FoodItems through the model ItemQuantity (defined right below).<br><br>

```Python

class ItemQuantity(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    rating = models.FloatField(default=5.0)
    food_id = models.ForeignKey(FoodItems, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.quantity} of {self.food_id} was ordered by {self.order_id}"

```
The model ItemQuantity stores the order_id and the food_id alongwith the rating found when Feedback is collected. It also stores the quantity of an item bought in a particular order.<br><br>
<h3>Models defined in the customer application</h3>

```Python

def unique_key_generator():
    length = random.randint(5, 10)
    secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return secret_code


class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10, auto_created=True, default=unique_key_generator)
    by = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.DO_NOTHING, blank=True, null=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

```
The model Feedback stores the feedback given by a customer.<br><br>

```Python

class Cart(models.Model):
    item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(EverydayOffers, on_delete=models.CASCADE, null=True, blank=True)

```
The model Cart stores the items currently in the Cart of a particular customer / cashier's order. We can use the filter() function of the model objects to find the items of a particular cart<br><br>

```Python

class Credit(models.Model):
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    last_date_of_add = models.DateTimeField(auto_now=True)

```
The model Credit stores the credit of a particular customer. Every time the customer signs up, credit object is initialized.<br><br>
<h2>App names and descriptions</h2>
<i>Access</i> - for login and registration<br>
<i>Home</i> - for homepage and redirections from there<br>
<i>Cashier</i> - for cashier related functionalities<br>
<i>Manager</i> - For manager related functionalities<br>
<i>Customers</i> - For customer related functionalities<br>
<h2>Details about the responsibilities given to different types of users</h2>
<h3>Admin</h3>
<p>The admin can delete any data pertaining to any user, fooditem, order etc.<br>The admin module uses frontend from the <i><a href="https://django-grappelli.readthedocs.io/en/latest/#">Grapelli</a></i> application of django.</p>
<h3>Manager</h3>
<p>The manager can Add, Update, Delete and View any food item. The constraint applied on the addition of a food item is that an item cannot be repeated, we check for the name of the food item being added to achieve this. <br>The manager can also Add, Update, Delete and View a offer. <br>With this, the manager is also allowed to view feedback provided by users. <br>A manager is also allowed to remove any cashier. The feature of deleting their own account has not been given to a cashier.<br>A manager can only sign up after providing the secret code sent on an admin's Email ID.</p>
<h3>Cashier</h3>
<p>A cashier can view food items along with place an order for a customer. Since they can place an order, they are obviously allowed to view their cart. A very important feature added here is that a cashier can apply a single offer depending on the 2 factors, one, any offer can be applied only once, and two, the offers visible/applicable are only on the items in cart. The display has been fixed this way.<br>A Cashier can also add credit for a customer in case a customer would want to exchange cash for credit.<br>A cashier is also allowed to delete a Customer's account.<br>A cashier can also download the bill of an order in PDF form.<br>A cashier can create their account if and only if a Manager gives them a secret code which is sent to them on their Email Address.</p>
<h3>Customer</h3>
<p>A customer can place an order by adding items to the cart and can also edit the items in the cart.<br>They can also apply any one offer at a time and place the order.<br>The customer can also add feedback for any order that they have previously placed with the constraint of being allowed to give feedback only once. They can view their feedback as well.<br>The customer can also add credit to their account and are also allowed to close their own account.<br>A very important feature that a customer is entitled to is, a customer can download the zip folder of their coupons which are in JPG format and they look like this.</p>

![TJsJBFFvNY_noodles](https://user-images.githubusercontent.com/63162622/139084257-4413ea4a-5be8-4ea2-bc27-dbbe2a2bbf6d.jpg)

<p>The users already in the database which can be used for testing</p>

<center>
<h4>Admin</h4>
<div style="border: 1px solid black; text-align: center; height: 60px; width: 400px; padding: 10px;">Email : nircas.official@gmail.com<br>
	User name : admin<br>
	Password : Password123#
</div>

<h4>Manager</h4>
<div style="border: 1px solid black; text-align: center; height: 60px; width: 400px; padding: 10px;">Email : ishikagititems@gmail.com<br>
	Password : Password123#
</div>

<h4>Cashier</h4>
<div style="border: 1px solid black; text-align: center; height: 60px; width: 400px; padding: 10px;">Email : veera_kapoor@gmail.com<br>
	Password : Password123#
</div>

<h4>Customer</h4>
<div style="border: 1px solid black; text-align: center; height: 100px; width: 400px; padding: 10px;">Email : ishikaishu2000@gmail.com<br>
	Password : Password123#
	<br><br>
	Email : palashshah@gmail.com<br>
	Password : Password123#
</div>
</center>


<h2>Steps to run the application</h2>
<ol>
	<li>First, download the zip or use the `git clone` command to get the source code in your local system</li>
	<li>Next navigate to the repository's location in a command prompt</li>
	<li>Next, run the command, `pip install -r nircas_adf\requirements.txt`.</li>
	<li>After this, we are ready to make the migrations, so run `python manage.py makemigrations`. After this run, `python manage.py migrate`.</li>
	<li>Last and final step, run the command, `python manage.py runserver` and you are ready to use the website. Hope you like it.</li>
</ol>
<br>
Collaborators : <br>
	<a href="https://github.com/krishnashah29">Krishna Shah</a><br>
	<a href="https://github.com/GreevaKhant1708">Greeva Khant</a><br>
	
