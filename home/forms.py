from django.forms import ModelForm, widgets
from django import forms
from .models import *

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        widgets = {
            'ngo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            
            
        }