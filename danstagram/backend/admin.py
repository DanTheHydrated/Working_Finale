from django.contrib import admin
from .models import Profile, Post
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):    
    model = Profile
    list_display = ['email', 'first_name', 'username']

admin.site.register(Profile, CustomUserAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Post)
