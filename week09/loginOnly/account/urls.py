# -*- coding:utf-8 -*-
from django.urls import path

from .views import index, logout, login, register

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
]
