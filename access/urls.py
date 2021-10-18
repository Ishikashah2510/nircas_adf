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
    url(r'^forgot_password/$', forgot_password, name='forgot_password'),
    url(r'^forgot_pass_mail/$', forgot_pass_email, name='forgot_pass_mail'),
    url(r'^home/', include('home.urls'))
]
