from django.shortcuts import render, redirect
from access import user_object
from access.models import *

# Create your views here.


def homepage(request):
    try:
        curr_user = Users.objects.get(email=request.session['curr_user'])
        return render(request, 'home/homepage.html', {'obj': curr_user})
    except:
        pass
    return render(request, 'home/homepage.html')
