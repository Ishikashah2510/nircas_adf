from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'customer'

urlpatterns = [
    url(r'^view_offer/$', view_offer, name="view_offer"),
    url(r'^delete_account/$', delete_account, name="delete_account"),
    url(r'^view_items/$', view_items, name="view_items"),
    url(r'add_to_cart/$', add_to_cart, name="add_to_cart"),
    url(r'^view_cart/$', view_cart, name="view_cart"),
    path(r'^place_order/(?P<total_cost>[0-9])/$', place_order, name="place_order"),
    url(r'^view_orders/$', view_orders, name="view_orders"),
    url(r'^add_credit/$', add_credit, name="add_credit"),
    url(r'^view_feedback/$', view_feedback, name="view_feedback"),
    url(r'^add_feedback/(?P<order_id>\w+)/$', add_feedback, name="add_feedback"),
    path(r'^apply_coupon/<int:pk>/$', apply_coupon, name="apply_coupon"),
    path(r'decrease_from_cart/(?P<name>\w+)', decrease_from_cart, name="decrease_from_cart"),
    path(r'increase_from_cart/(?P<name>\w+)', increase_from_cart, name="increase_from_cart"),
]
