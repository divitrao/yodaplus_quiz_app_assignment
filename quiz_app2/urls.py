from django.urls import path,include
from .views import first, form_test ,rules_page, quiz_challenge
urlpatterns = [
    path('',first.as_view(),name = 'home'),
    path('add/',form_test.as_view(),name='form_test'),
    path('rules',rules_page.as_view(),name='rules_page'),
    path('challenge',quiz_challenge.as_view(),name='challenge')
]