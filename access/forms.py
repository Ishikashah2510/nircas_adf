from django import forms
from .models import *
from django.forms import ModelForm, BaseModelForm, BaseForm
from django.utils.safestring import mark_safe


class LoginForm(forms.Form):
    user_types = [
        ('Customer', 'Customer'),
        ('Cashier', 'Cashier'),
        ('Manager', 'Manager')
    ]
    email_ = forms.EmailField(label=mark_safe('Email ID<br>'),
                              label_suffix='',
                              widget=forms.TextInput(attrs={'placeholder': 'johndoe@unknown.com',
                                                            'size': 30, 'style': 'height: 24px'}))
    password_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Top secret key here🤫',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                label=mark_safe('Password<br>'),
                                label_suffix='')
    user_type = forms.ChoiceField(label=mark_safe('Which user are you?<br>'),
                                  label_suffix='',
                                  choices=user_types,)


class RegistrationFormCust(ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email', 'birthdate', 'mobile_no', 'password', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jane Doe',
                                           'size': 26, 'style': 'height: 24px',},),
            'email': forms.EmailInput(attrs={'placeholder': 'janedoe@incognito.com',
                                            'size': 26, 'style': 'height: 24px', }, ),
            'birthdate': forms.DateInput(attrs={'type':'date', 'required': True}),
            'mobile_no': forms.TextInput(attrs={'placeholder': '9182736450',
                                                'size': 26, 'style': 'height: 24px', }, ),
            'password': forms.PasswordInput(attrs={'placeholder': 'Open Sesame code',
                                               'size': 26, 'style': 'height: 24px', }, ),
        }

    repassword_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Open Sesame code',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                  label=mark_safe('Re-enter password: '),
                                  label_suffix='')


class UserChoiceForm(ModelForm):
    class Meta:
        model = Users
        fields = ('user_type', )


class RegistrationFormCash(ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email', 'birthdate', 'mobile_no', 'password', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jane Doe',
                                           'size': 26, 'style': 'height: 24px',},),
            'email': forms.EmailInput(attrs={'placeholder': 'janedoe@incognito.com',
                                            'size': 26, 'style': 'height: 24px', }, ),
            'birthdate': forms.DateInput(attrs={'type':'date', 'required': True}),
            'mobile_no': forms.TextInput(attrs={'placeholder': '9182736450',
                                                'size': 26, 'style': 'height: 24px', }, ),
            'password': forms.PasswordInput(attrs={'placeholder': 'Open Sesame code',
                                               'size': 26, 'style': 'height: 24px', }, ),
        }

    repassword_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Open Sesame code',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                  label=mark_safe('Re-enter password: '),
                                  label_suffix='')
    manager_eid = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'janedoe@incognito.com',
                                            'size': 26, 'style': 'height: 24px', },),
                                    label=mark_safe('Manager Email ID'),
                                    label_suffix='')
    UniqueCode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unique code sent on manager email ID',
                                                               'size': 26, 'style': 'height: 24px',},),
                                 label=mark_safe('Unique Code'),
                                 label_suffix='')


class RegistrationFormMan(ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'email', 'birthdate', 'mobile_no', 'password', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jane Doe',
                                           'size': 26, 'style': 'height: 24px',},),
            'email': forms.EmailInput(attrs={'placeholder': 'janedoe@incognito.com',
                                            'size': 26, 'style': 'height: 24px', }, ),
            'birthdate': forms.DateInput(attrs={'type':'date', 'required': True}),
            'mobile_no': forms.TextInput(attrs={'placeholder': '9182736450',
                                                'size': 26, 'style': 'height: 24px', }, ),
            'password': forms.PasswordInput(attrs={'placeholder': 'Open Sesame code',
                                               'size': 26, 'style': 'height: 24px', }, ),
        }

    repassword_ = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Open Sesame code',
                                                                                 'size': 26, 'style': 'height: 24px',
                                                                                 }),
                                  label=mark_safe('Re-enter password: '),
                                  label_suffix='')
    admin_eid = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'janedoe@incognito.com',
                                                                   'size': 26, 'style': 'height: 24px', }, ),
                                    label=mark_safe('Admin Email ID'),
                                    label_suffix='')
    UniqueCode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unique code sent on admin email ID',
                                                               'size': 26, 'style': 'height: 24px', }, ),
                                 label=mark_safe('Unique Code'),
                                 label_suffix='')
