from django import forms
from .models import *
from customer.models import *


class AddCreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = '__all__'


class DeleteCustomerForm(forms.Form):
    user_id = forms.ModelChoiceField(queryset=Users.objects.filter(user_type='Customer'))
