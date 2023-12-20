from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import render, redirect

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=20, null = True)
    email = models.EmailField(max_length=50, null = True)
    password = models.CharField(max_length=50, null = True)
    origin_date = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name
