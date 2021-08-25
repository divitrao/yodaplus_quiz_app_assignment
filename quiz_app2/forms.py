from django import forms
from django.db.models import fields
from django.forms import widgets
from django import forms
from django.forms.fields import IntegerField
from .models import model_tests

class Addform(forms.ModelForm):
    class Meta:
        model = model_tests
        fields = ('fav_sub','user_id')

        widgets = {
            'fav_sub':forms.TextInput(),
            'user_id':forms.TextInput(attrs={'id': 'users'}),
            
        }

class Myyform(forms.Form):
    I_Accept_Rules_and_Regulation = forms.BooleanField(required=True)

        