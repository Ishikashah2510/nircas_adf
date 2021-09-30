from django.conf.urls import url
from django.urls import path, include
from .views import *

app_name = 'access'

urlpatterns = [
    url('^$', go_to_homepage, name='homepage'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^user_choice/$', user_type_redirect, name='user_choice'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^home/', include('home.urls'))
]
