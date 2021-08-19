from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import Addform
# Create your views here.

class first(TemplateView):
    template_name = 'home.html'

class form_test(FormView):
    template_name = 'add.html'
    form_class = Addform
    success_url = '/'

    def form_valid(self, form ):
        form.save()
        return super().form_valid(form)
# class form_test(TemplateView):
#     template_name = 'add.html'

