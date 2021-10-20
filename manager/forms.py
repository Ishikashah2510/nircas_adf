from django import forms
from .models import *


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = '__all__'
        exclude = ('rating',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "What's my name?😋"}),
            'cost': forms.NumberInput(attrs={'placeholder': '₹ 99.99',},),
            'description': forms.Textarea(attrs={'placeholder': 'Describe me',
                                                 'style': 'height: 40px', }),
            'serves': forms.NumberInput(attrs={'placeholder': 'How many people am I sufficient for?',
                                               'size': 40, 'style': 'width: 250px'})
        }


class UpdateFoodForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = ('name', 'description', 'serves', 'cost')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "What's my name?😋", "readonly": True}),
            'cost': forms.NumberInput(attrs={'placeholder': '₹ 99.99', }, ),
            'description': forms.Textarea(attrs={'placeholder': 'Describe me',
                                                 'style': 'height: 40px', }),
            'serves': forms.NumberInput(attrs={'placeholder': 'How many people am I sufficient for?',
                                               'size': 40, 'style': 'width: 250px'})
        }


class AddOfferForm(forms.ModelForm):
    class Meta:
        model = EverydayOffers
        fields = '__all__'
        widgets = {
            'discount': forms.NumberInput(attrs={'placeholder': '25%', }, ),
        }


class UpdateOfferForm(forms.ModelForm):
    class Meta:
        model = EverydayOffers
        fields = ('discount', )
