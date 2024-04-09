from .views import BlogList, BlogDetail, AddView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', BlogList.as_view(), name='blog'),
    path('article/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
    path('add_post/', AddView.as_view(), name='add_post'),

]
