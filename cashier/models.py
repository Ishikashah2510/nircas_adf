from django.db import models
from access.models import *
from manager.models import *
from datetime import datetime
import random
import string

# Create your models here.


def unique_key_generator():
    length = random.randint(5, 10)
    secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return secret_code


class Orders(models.Model):
    order_id = models.CharField(max_length=10, unique=True, default=unique_key_generator)
    user_id = models.ForeignKey(Users, limit_choices_to={'user_type': 'Customer'}, on_delete=models.CASCADE)
    total_cost = models.FloatField()
    items = models.ManyToManyField(FoodItems)
    order_date = models.DateTimeField(auto_now=True)
