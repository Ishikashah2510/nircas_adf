from django.shortcuts import render, redirect
from access import user_object

# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html', {'obj': user_object.curr_user})

