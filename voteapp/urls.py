from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index.html'),
    path('getquery',views.getquery,name='getquery'),
    path('/sortdata',views.sortdata,name= 'sortdata'),
]