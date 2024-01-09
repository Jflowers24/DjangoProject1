from django.contrib import admin

# Register your models here.
from .models import Account, Post

admin.site.register(Account)
admin.site.register(Post)
