from django.urls import path,include
from .views import first, form_test
urlpatterns = [
    path('',first.as_view(),name = 'home'),
    path('add/',form_test.as_view(),name='form_test')
]