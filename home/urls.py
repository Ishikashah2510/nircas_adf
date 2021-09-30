from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    url(r'^homepage/$', homepage, name='homepage'),
]
