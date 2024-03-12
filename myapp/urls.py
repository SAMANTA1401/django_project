from django.urls import  path
from . import views

#1.
urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctioncallabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('intro/<str:name>/<str:age>', views.intro, name='intro'),
    path('index',views.index,name="index"),
    path('home',views.home,name="home"),
    path('first',views.first,name='first'),
    path('imagepage',views.imagepage, name='imagepage'),
    path('imagepage2/<str:imagename>',views.imagepage2, name='imagepage2'),
    path('myform',views.myform, name='myform'),
    path('submitform',views.submitform, name='submitform'),
    path('form2',views.myform2, name='myform2')

]