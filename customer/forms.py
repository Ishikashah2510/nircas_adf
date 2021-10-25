from django import forms
from .models import *
from cashier.models import *


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message', 'by')

        widgets = {
            'by' : forms.HiddenInput(attrs={'value': ''})
        }
