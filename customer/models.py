from django.db import models
from access.models import *
from cashier.models import *
from manager.models import *


# Create your models here.


class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10)
    by = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    rating_for_food = models.FloatField()
    message = models.CharField(max_length=255)


class Cart(models.Model):
    items = models.ManyToManyField(FoodItems)
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(EverydayOffers, on_delete=models.CASCADE)


class Credit(models.Model):
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    last_date_of_add = models.DateTimeField(auto_now=True)
