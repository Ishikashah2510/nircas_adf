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
<h3>Models in <i>access</i> application</h3>
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">class</span> <span style="color: #BB0066; font-weight: bold">Users</span>(models<span style="color: #333333">.</span>Model):
    user_types <span style="color: #333333">=</span> [
        (<span style="background-color: #fff0f0">&#39;Customer&#39;</span>, <span style="background-color: #fff0f0">&#39;Customer&#39;</span>),
        (<span style="background-color: #fff0f0">&#39;Cashier&#39;</span>, <span style="background-color: #fff0f0">&#39;Cashier&#39;</span>),
        (<span style="background-color: #fff0f0">&#39;Manager&#39;</span>, <span style="background-color: #fff0f0">&#39;Manager&#39;</span>)
    ]
    name <span style="color: #333333">=</span> models<span style="color: #333333">.</span>CharField(max_length<span style="color: #333333">=</span><span style="color: #0000DD; font-weight: bold">100</span>)
    email <span style="color: #333333">=</span> models<span style="color: #333333">.</span>EmailField(primary_key<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">True</span>)
    password <span style="color: #333333">=</span> models<span style="color: #333333">.</span>CharField(max_length<span style="color: #333333">=</span><span style="color: #0000DD; font-weight: bold">30</span>)
    birthdate <span style="color: #333333">=</span> models<span style="color: #333333">.</span>DateField(blank<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">True</span>, null<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">True</span>)
    mobile_no <span style="color: #333333">=</span> models<span style="color: #333333">.</span>IntegerField(unique<span style="color: #333333">=</span><span style="color: #008800; font-weight: bold">True</span>)
    user_type <span style="color: #333333">=</span> models<span style="color: #333333">.</span>CharField(choices<span style="color: #333333">=</span>user_types,
                                 default<span style="color: #333333">=</span><span style="background-color: #fff0f0">&#39;Customer&#39;</span>,
                                 max_length<span style="color: #333333">=</span><span style="color: #0000DD; font-weight: bold">9</span>)
</pre></div>
<br><br>
The above model, Users is used to store the details of each kind of user. It is a basic model with a choices list for user type
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
