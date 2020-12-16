from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('upload_file',views.upload,name="upload_file"),
    path('show_notes',views.show,name="show_notes"),
    path("text_notes",views.Upload_text_notes,name="text_notes"),
   
]