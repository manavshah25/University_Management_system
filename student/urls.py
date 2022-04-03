from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('addstudent', views.addstudent,name='addstudent'),
     
]