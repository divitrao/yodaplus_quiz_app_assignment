from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from .forms import Addform, Myyform
from .models import model_tests
# Create your views here.

class first(TemplateView):
    template_name = 'home.html'

# class form_test(FormView):
#     template_name = 'add.html'
#     form_class = Addform
#     success_url = '/'

#     def form_valid(self, form ):
#         form.save()
#         return super().form_valid(form)

class form_test(CreateView):
    template_name = 'add.html'
    form_class = Addform
    success_url = '/'

    # def get_context_data(self, **kwargs) :
    #     # test_ = model_tests
    #     # test_.user_id= self.request.user.id
    #     # test_.save(self)
    #     context = super().get_context_data(**kwargs)
    #     login_user_id = self.request.user.id
    #     context['ff'] = login_user_id
    #     print(context['ff'])
    #     return context
    def get_initial(self,*args,**kwargs):

        initial =  super().get_initial(**kwargs)
        initial['user_id'] = self.request.user.id
        print(model_tests.objects.filter(user_id=self.request.user.id).exists())
        return initial
     

# class form_test(TemplateView):
#     template_name = 'add.html'


class rules_page(FormView):
    template_name = 'rule.html'
    form_class = Myyform
    success_url = 'challenge'

    def form_valid(self, form):
        return super().form_valid(form)

class quiz_challenge(TemplateView):
    template_name = 'quiz_challenge.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

