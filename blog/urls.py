from .views import BlogList, BlogDetail
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', BlogList.as_view(), name='blog'),
    path('<int:pk>', BlogDetail.as_view(), name='blog_detail'),
]
