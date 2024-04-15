from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "mongocon"

urlpatterns = [
    path('',views.index,name='index'),
    path('/add_person',views.add_person,name='add_person'),
    path('/get_person',views.get_person,name="get_person"),
    path('upload_file',views.upload_file, name='upload_file'),
    path('download_file',views.download_file, name='download_file'),
    path('update_file/<str:name>',views.update_file, name='update_file'),
    path('update_submit_file/<str:name>',views.update_submit_file, name='update_submit_file'),
    path('delete_file/<str:name>',views.delete_file, name='delete_file'),
    path('read_file', views.read_file, name='read_file'),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

handler404 = 'mongocon.views.error_404_view'
