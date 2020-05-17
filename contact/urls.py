# -*- coding: utf-8 -*-
# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]
