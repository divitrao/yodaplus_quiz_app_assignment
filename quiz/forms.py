from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.db.models import fields

class Customer_user_creation_form(UserCreationForm):
    class Meta:
        models = get_user_model()
        fields = ('email','username',)


class Custom_user_change_form(UserChangeForm):
    class Meta:
        models = get_user_model()
        fields = ('email','username',)