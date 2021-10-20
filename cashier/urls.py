from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'cashier'

urlpatterns = [
    url(r'^trial/$', trial_view, name="trial")
]