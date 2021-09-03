from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import database_add_test
from .forms import Addit
# Create your views here.

class Add_data(CreateView):
    model = database_add_test
    form_class = Addit
    template_name = 'add_data.html'
    success_url = '/'

