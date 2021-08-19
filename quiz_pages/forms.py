from django import forms
from django.db.models import fields
from django.forms import widgets
from django import forms
from .models import model_test

class Addform(forms.ModelForm):
    class Meta:
        model = model_test
        fields = ('fav_sub',)

        widgets = {
            'fav_sub':forms.TextInput(),
        }