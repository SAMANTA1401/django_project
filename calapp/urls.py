from django.urls import path
from . import views


urlpatterns = [
    path('',views.calui,name='calui'),
    path('submitquery', views.submitquery, name= 'submitquery'),
]