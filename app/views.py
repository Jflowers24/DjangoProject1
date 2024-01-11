from django.shortcuts import render, get_object_or_404
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
from .decorators import unauthenticated_user, allowed_users, admins_only
from django.contrib.auth.models import User
from .forms import UpdateUsername





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
    

#@allowed_users(allowed_roles=['Admins','Users'])

def Home(request: HttpRequest)-> HttpResponse:
    post = Post.objects.filter(User=request.user).last()

    return render(request,"home.html", {post:'post'})

@allowed_users
def userpage(request):
    context = {}
    return render(request, 'accounts/user.html', context)


def logoutuser(request):
    logout(request)
    return redirect('/')


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



@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

@login_required
def updateName(request):
    if request.method == 'POST':
        form = UpdateUsername(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            # request.user.Username = new_username
            # request.user.save()
            user = User.objects.get(username = request.user)
            user.username = new_username
            user.save()
            return redirect('/')
        
    else:
        form = UpdateUsername
    return render(request, 'updateUsername.html', {'form':form})

@login_required
def delete_posts(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.User == request.user:
        post.delete()
    return redirect('home')

@login_required
def usersposts(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        return delete_posts(request, post_id)
    
    return render(request, 'delete.html', {'posts':posts})


@admins_only
def admin_page(request):
    posts = Post.objects.all()

    return render(request, 'Admin.html', {'posts':posts})






