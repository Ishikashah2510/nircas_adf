from django.shortcuts import render, redirect
from access.user_object import *

# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html', {'obj': curr_user})

