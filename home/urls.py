from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    url(r'^homepage/$', homepage, name='homepage'),
    url(r'manager/', include('manager.urls')),
    url(r'cashier/', include('cashier.urls')),
    url(r'customer/', include('customer.urls')),
]
