from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date
from access.isValidPassword import *
from . import user_object
from home.views import *
from access.send_email import *
from customer.models import *

# Create your views here.''


def go_to_homepage(request):
    return render(request, 'access/homepage.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                curr_user = Users.objects.get(email=form.cleaned_data['email_'],
                                              password=form.cleaned_data['password_'],
                                              user_type=form.cleaned_data['user_type'])
                curr_user.is_user_authenticated(True)
                request.session['curr_user'] = curr_user.email
                request.session['user_type'] = form.cleaned_data['user_type']
                request.session.set_expiry(300)
                return HttpResponseRedirect('/home/homepage/')
            except Exception as e:
                print(form.cleaned_data['email_'], form.cleaned_data['password_'], form.cleaned_data['user_type'])
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
                okay, message = data_okay(form, request.POST.get('unique_id'), request)
                if okay:
                    if request.session['user_type'] == 'Customer':
                        c = Credit(user_id=Users.objects.get(email=form.cleaned_data['email']))
                        c.save()
                    form = LoginForm()
                    return render(request, 'access/login.html', {'message': 'Account created successfully!',
                                                                 'form': form})
                else:
                    return render(request, 'access/register.html', {'message': message, 'form': form,
                                                                    'user_type': request.session['user_type']})
        except Exception as e:
            print(e)
            return render(request, 'access/register.html', {'form': form, 'message': 'Data entered is invalid',
                                                            'user_type': request.session['user_type']})
    form = RegistrationForm()

    return render(request, 'access/register.html', {'form': form,
                                                    'user_type': request.session['user_type']})


def data_okay(form, uniqueid, request):
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

    if request.session['user_type'] != 'Customer' and not uniqueid == request.session['secret_code']:
        message = 'The unique ID entered is wrong, enter it again'
        return False, message

    if not send_mail_register(form.cleaned_data['email'], form.cleaned_data['name']):
        message = 'Seems like you have entered a invalid email ID'
        return False, message

    form = form.save(commit=False)
    form.user_type = request.session['user_type']
    form.save()

    return True, 'Okay'


def user_type_redirect(request):
    if request.method == 'POST':
        hidden_val = request.POST.get('formval')

        if hidden_val == '1':
            form = UserChoiceForm(request.POST)
            print(form)
            request.session['user_type'] = form.cleaned_data['user_type']

            if form.cleaned_data['user_type'] == 'Customer':
                if form.is_valid():
                    form = RegistrationForm()
                    return render(request, 'access/register.html', {'form': form})

            else:
                form = UserChoiceForm(initial={'user_type': request.session['user_type']})
                return render(request, 'access/register_user.html', {'form': form, 'x': 1})

        elif hidden_val == '2':
            if send_mail(request.POST.get('email_'), request.session['user_type'], request):
                return register(request)
            else:
                form = UserChoiceForm(initial={'user_type': request.session['user_type']})
                return render(request, 'access/register_user.html', {'form': form, 'x': 1,
                                                                     'message': 'Entered ID is not of your supervisor'})

    form = UserChoiceForm()
    return render(request, 'access/register_user.html', {'form': form})


def logout(request):
    try:
        curr_user = Users.objects.get(email=request.session['curr_user'])
        curr_user.is_user_authenticated(False)
        request.session.flush()

    except:
        pass
    return HttpResponseRedirect('/login/')


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        try:
            if form.is_valid():
                okay, msg = valid_data(form)
                if okay:
                    u = Users.objects.get(email=request.session['fp_email'])
                    u.password = form.cleaned_data['password_']
                    u.save()
                    return HttpResponseRedirect('/login/')
                else:
                    form = ForgotPasswordForm()
                    return render(request, 'access/forgot_password.html', {'message': msg, 'form': form})
        except Exception as e:
            print(e)
            return render(request, 'access/forgot_password.html', {'message': 'Data entered is invalid',
                                                                   'form': form})

    form = ForgotPasswordForm()
    return render(request, 'access/forgot_password.html', {'form': form})


def valid_data(form):
    try:
        u = Users.objects.get(email=form.cleaned_data['email_'])
        return False, "No user exists with the given email ID, are you sure the input is correct?"
    except:
        pass
    if form.cleaned_data['password_'] != form.cleaned_data['repassword_']:
        return False, 'The passwords do not match, kindly re-enter them'

    if not isValidPassword(form.cleaned_data['password_']):
        password_valid_string = '''Your password must contain
        at least 1 digit, 1 capital letter, 
        and at least one of _#!$%&*'''
        return False, password_valid_string

    return True, ''


def forgot_pass_email(request):
    if request.method == 'POST':
        email = request.POST.get('email_')
        send_forgot_pass_mail(email)
        request.session['fp_email'] = email
        return HttpResponseRedirect('/forgot_password/')
    return render(request, 'access/forgot_password.html')
