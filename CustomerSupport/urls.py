from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('support', views.support, name='support'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path("logout", views.logout_request, name="logout"),

]