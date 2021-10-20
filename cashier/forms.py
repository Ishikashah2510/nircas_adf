from django import forms
from .models import *


class TrialForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
