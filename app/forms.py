from django.forms import ModelForm 
from .models import Account, Post
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Description', 'User']
        
