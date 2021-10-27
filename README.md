# nircas_adf
NIRCAS - Nirma Canteen Automation System
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
		<li>we have proposed a 3 level heirarchy in the maintenance of the website with user types like 'Admin', 'Manager', 'Cashier' and 'Customer'. More details have been described below.</li>
	</ul>
</p>
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

