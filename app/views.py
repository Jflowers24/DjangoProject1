from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.:
from .models import *
from .forms import Account, PostForm
from .forms import CreateUserForm
from .forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import User




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

@allowed_users
def userpage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("test")
            postie = form.save(commit=False)
            postie.User = request.user
            postie.save()
            
            
            return redirect('post_list')
        
    return render(request, 'post.html', {'form': form})




def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


