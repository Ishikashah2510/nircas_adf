from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'manager'

urlpatterns = [
    url(r'^homepage/$', homepage, name="homepage"),
    url(r'^add_fooditem/$', additem, name="add_fooditem"),
    url(r'^view_fooditem/$', view_items, name="view_fooditem"),
    url(r'^update_fooditem/$', update_item, name="update_fooditem"),
    url(r'^update_withform/$', update, name="update_withform"),
    path(r'^delete_fooditem/<int:pk>/$', delete_fooditem, name="delete_fooditem"),
    url(r'^add_offer/$', add_offer, name="add_offer"),
    url(r'^view_offer/$', view_offer, name="view_offer"),
    url(r'^update_offer/$', update_offer, name="update_offer"),
    path(r'^delete_offer/<int:pk>/$', delete_offer, name="delete_offer"),
]
