# -*- coding: utf-8 -*-
# users/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    ## Repath uses REGEX (regular expression path) to create unique one time url
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('activation_success/', views.activation_success, name='activation_success'),
    path('activation_invalid/', views.activation_invalid, name='activation_invalid'),
]
