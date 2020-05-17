from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(BaseUserAdmin):
    ''' Class that extends BaseUserAdmin.'''
    model = CustomUser
    '''Forms that add and change user instances'''
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    '''Displayed fields from CustomUser. Overrides definitions in BaseUserAdmin that references auth.User.'''
    list_display = ('email', 'full_name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')

    list_filter = ('last_login', 'date_joined', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions',)})
    )

    '''# add_fieldsets is not a standard ModelAdmin attribute.
    UserAdmin overrides get_fieldsets to use this attribute when creating a user.'''
    add_fieldsets = (
        (None, {'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_active', 'is_staff',
                'is_superuser', 'password1', 'password2')}),
    )

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('-last_login',) ## Or any other field as preferred

    filter_horizontal = ()

''' Registers CustomUser and CustomUserAdmin '''
admin.site.register(CustomUser, CustomUserAdmin)
