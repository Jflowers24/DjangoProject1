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
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(initial={"User": request.user})
        if form.is_valid():
            postie = form.save(commit=False)
            print(form.User)
            postie.User = request.User
            postie.save
            
            return redirect(post_list)
        else:
            form = PostForm()
    return render(request, 'post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


