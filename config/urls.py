"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app.views import Register, Home, userpage,  logoutuser, post_list, createPost, updateName, usersposts, delete_posts, admin_page
from django.contrib.auth.views import LoginView 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html")),
    path('logout/', logoutuser, name="logout"),
    path("", Register),
    path("home/", Home, name="home"),
    path("accounts/profile/",Home),
    path('user/', userpage, name='user-page'),
    path('Posts/', post_list, name = 'post_list'),
    path('CreatePost/', createPost, name = 'create_post' ),
    path('UpdateUsername/', updateName, name ='update_username'),
    path('DeletePost/', usersposts, name='deletepost'),
    path('delete_posts/<int:post_id>/', delete_posts, name='dp'),
    path('AdminBabay/', admin_page, name='adminnn')


]
