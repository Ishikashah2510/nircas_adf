from django.db import models
from access.models import *
from cashier.models import *

# Create your models here.


class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10)
    by = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    rating_for_food = models.FloatField()
    message = models.CharField(max_length=255)
