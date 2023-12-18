from django.forms import ModelForm 
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Account(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'email', 'password']
        