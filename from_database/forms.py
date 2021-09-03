from django import forms
from django.forms import fields, widgets
from .models import database_add_test


class Addit(forms.ModelForm):
    class Meta:
        model = database_add_test
        fields = ('question','answer','option_1','option_2','option_3')
        Widgets ={
            'question' : forms.Textarea(),
            'answer': forms.TextInput(),
            'option_1': forms.TextInput(),
            'option_2': forms.TextInput(),
            'option_3': forms.TextInput(),
        }