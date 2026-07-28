from django.urls import path 
from . import views #from current directory import views

urlPatterns = [
    path('function', views.hello_world ),
    path('class', views.HelloEthiopia.as_view())
]