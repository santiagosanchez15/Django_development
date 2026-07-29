from django.urls import path 
from . import views #from current directory import views

urlpatterns = [
    path('llama', views.hello_world ),
    path('class', views.HelloEthiopia.as_view()), 
    path('reservation', views.home),
]