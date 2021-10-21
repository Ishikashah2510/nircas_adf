from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'cashier'

urlpatterns = [
    url(r'^add_credit/$', add_credit, name="add_credit"),
    url(r'^delete_customer/$', del_cust_account, name="delete_customer"),
]