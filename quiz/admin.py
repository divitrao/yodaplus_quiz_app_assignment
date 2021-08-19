from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import Custom_user_change_form,Customer_user_creation_form

# Register your models here.

custom_user = get_user_model()

class custom_user_admin(UserAdmin):
    add_form = Customer_user_creation_form
    form = Custom_user_change_form
    model = custom_user
    list_display = ['email','username']

admin.site.register(custom_user,custom_user_admin)