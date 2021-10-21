from django.contrib import admin
from customer.models import *
from .models import *

# Register your models here.
admin.site.register(Cart)
admin.site.register(Feedback)
admin.site.register(Credit)
