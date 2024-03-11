from django.urls import  path
from . import views

#1.
urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctioncallabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('intro/<str:name>/<str:age>', views.intro, name='intro'),
    path('index',views.index,name="index")

]