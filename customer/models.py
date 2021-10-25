from django.db import models
from access.models import *
from cashier.models import *
from manager.models import *
import string
import random


# Create your models here.


def unique_key_generator():
    length = random.randint(5, 10)
    secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return secret_code


class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10, auto_created=True, default=unique_key_generator)
    by = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.DO_NOTHING, blank=True, null=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)


class Cart(models.Model):
    item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(EverydayOffers, on_delete=models.CASCADE, null=True, blank=True)


class Credit(models.Model):
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    last_date_of_add = models.DateTimeField(auto_now=True)
