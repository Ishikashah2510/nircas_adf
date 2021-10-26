from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from access import user_object
from access.models import *

# Create your views here.


def homepage(request):
    try:
        curr_user = Users.objects.get(email=request.session['curr_user'])
        if request.session['user_type'] == 'Manager':
            return HttpResponseRedirect('/home/manager/homepage/')
        elif request.session['user_type'] == 'Customer':
            return HttpResponseRedirect('/home/customer/homepage/')
    except:
        pass

    html_string = '''<html>
    <body><center>
    <br><br>
    <h1>Kindly sign in at <a href='http://127.0.0.1:8000/login/'>http://127.0.0.1:8000/login/</a></h1>
    </center></body>
    </html>'''
    return HttpResponse(html_string)
