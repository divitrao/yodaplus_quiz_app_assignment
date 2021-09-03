from django.urls import include,path
from .views import Add_data

urlpatterns = [
    path('',Add_data.as_view(),name='add_data')
]