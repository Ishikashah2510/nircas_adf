from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date
from access.isValidPassword import *
from . import user_object
from home.views import *

# Create your views here.''


def go_to_homepage(request):
    return render(request, 'access/homepage.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user_object.curr_user = Users.objects.get(email=form.cleaned_data['email_'],
                                              password=form.cleaned_data['password_'],
                                              user_type=form.cleaned_data['user_type'])
                curr_user.is_user_authenticated(True)
                return redirect('/home/homepage/', {'obj': curr_user})
            except Exception as e:
                print(e)
                return render(request, 'access/login.html', {'form': form, 'message': 'Forgot your password?'})
        else:
            return render(request, 'access/login.html', {'form': form, 'message': 'Not cool'})
    else:
        form = LoginForm()

    return render(request, 'access/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        try:
            if form.is_valid():
                okay, message = data_okay(form)
                if okay:
                    form = LoginForm()
                    return render(request, 'access/login.html', {'message': 'Account created successfully!',
                                                                 'form': form})
                else:
                    return render(request, 'access/register.html', {'message': message, 'form': form,
                                                                    'user_type': user_object.user_type})
        except Exception as e:
            print(e)
            return render(request, 'access/register.html', {'form': form, 'message': 'Data entered is invalid',
                                                            'user_type': user_object.user_type})
    form = RegistrationForm()

    return render(request, 'access/register.html', {'form': form,
                                                    'user_type': user_object.user_type})


def data_okay(form):
    q1 = Users.objects.filter(Q(email=form.cleaned_data['email']) | Q(mobile_no=form.cleaned_data['mobile_no']))
    if q1:
        return False, 'Account already exists'

    if form.cleaned_data['password'] != form.cleaned_data['repassword_']:
        return False, 'Passwords do not match'

    birthDate = form.cleaned_data['birthdate']
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    if age < 18:
        return False, 'Too young to join Connectify'

    if not isValidPassword(form.cleaned_data['password']):
        password_valid_string = '''Your password must contain
        at least 1 digit, 1 capital letter, 
        and at least one of _#!$%&*'''
        return False, password_valid_string

    form.save()
    return True, 'Okay'


def user_type_redirect(request):
    if request.method == 'POST':
        hidden_val = request.POST.get('formval')
        if hidden_val == '1':
            form = UserChoiceForm(request.POST)
            print(form)
            if form.cleaned_data['user_type'] == 'Customer':
                if form.is_valid():
                    user_object.user_type = 'Customer'
                    form = RegistrationForm()
                    return render(request, 'access/register.html', {'form': form})
            else:
                user_object.user_type = form.cleaned_data['user_type']
                form = UserChoiceForm(initial={'user_type': form.cleaned_data['user_type']})
                return render(request, 'access/register_user.html', {'form': form, 'x': 1})
        elif hidden_val == '2':
            # send_email(request.POST.get('email_'))
            return register(request)
    form = UserChoiceForm()
    return render(request, 'access/register_user.html', {'form': form})


def logout(request):
    curr_user.is_user_authenticated(False)
    return login(request)


def trial_view(request):
    print('Hello, banana!')
