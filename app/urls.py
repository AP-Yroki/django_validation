from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.register),
    path('login/', views.login),
]