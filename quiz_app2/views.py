from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from .forms import Addform, Myyform, user_choice
from .models import model_tests
from json import dumps
# Create your views here.

class first(FormView):
    q_count ='10'
    cat = 'any'
    diff='any'
    type = 'any'
    template_name = 'home.html'
    form_class = user_choice
    success_url = 'rules'
    def form_valid(self, form):
        first.q_count = self.request.POST.get('Number_of_question')
        first.cat  = self.request.POST.get('category')
        first.diff  = self.request.POST.get('difficulty')
        first.type = self.request.POST.get('Q_type')
        # print(first.q_ee)
        # print(self.request.POST.get('Number_of_question'))
        # print(self.request.POST.get('category'))
        # print(self.request.POST.get('difficulty'))
        # print(self.request.POST.get('Q_type'))
        return super().form_valid(form)


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

class quiz_challenge(TemplateView,first):
    template_name = 'quiz_challenge.html'
    \
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_dict = {'question_count':first.q_count,
                     'category ':first.cat,
                     'difficulty ':first.diff,
                     'type':first.type }
        print('question_count',first.q_count)
        print('category ',first.cat)
        print('difficulty ',first.diff)
        print('type',first.type)
        context['data']  = dumps(data_dict)
        return context
    



