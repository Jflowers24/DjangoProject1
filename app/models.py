from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User



# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, null = True)
    email = models.EmailField(max_length=50, null = True)
    password = models.CharField(max_length=50, null = True)
    origin_date = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    Title = models.CharField(max_length=60, null = True)
    Description = models.CharField(max_length=3000, null = True)
    Image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Title


