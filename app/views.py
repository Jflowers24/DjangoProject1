from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.:
from .models import *
from .forms import Account


def Register(request):
    form = Account()

    if request.method == "POST":
        form = Account(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')

    context = {'form':form}
    return render(request, "Register.html", context)

def loginpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, name=name, password=password)


        if user:
            login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request,"login.html", context)
    

def Home(request: HttpRequest)-> HttpResponse:
    return render(request,"home.html")