from django.forms import ModelForm 
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django import forms




class CreateUserForm(UserCreationForm):
    pass