from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.:
from .models import *
from .forms import Account, Post
from .forms import CreateUserForm
from .forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def Register(request):
    
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')

    context = {'form':form}
    return render(request, "Register.html", context)
    

@allowed_users(allowed_roles=['Admins'])
def Home(request: HttpRequest)-> HttpResponse:
    return render(request,"home.html")

def userpage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def createPost(request):
    form = Post()

    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.User = request.User
            post.save()
            return redirect(post_list)
        

def post_list(request):
    ...