from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# users/models.py
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class CustomUserManager(BaseUserManager):
    '''Class that creates and saves a User with the given email, date of birth and password.'''
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password=None,):

        '''Method that creates and saves a User with the given email and password.'''
        if not email:
            raise ValueError("User's email is required")
        '''Normalise email, that is it converts domain to lowercase '''
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        '''Method that creates and saves an superuser with the given email and password.'''
        user = self.create_user(email, password=password, first_name=first_name, last_name=last_name,)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Class that describes a user with the given email and password.'''
    email = models.EmailField(('Email Address'), unique=True)
    first_name = models.CharField(('First Name'), max_length=60, blank=False)
    last_name = models.CharField(('Last Name'), max_length=60, blank=False)
    last_login = models.DateTimeField(('Last login'), auto_now=True)
    date_joined = models.DateTimeField(('Date joined'), auto_now_add=True)
    user_id_revised_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(('Active'), default=True)
    is_staff = models.BooleanField(('Staff'), default=False)
    is_superuser = models.BooleanField(('Super'), default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ''' Class to support search functions.'''
        ordering = ["-user_id_revised_date"]
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def short_name(self):
        '''Method that returns the user's first name.'''
        return self.first_name

    def full_name(self):
        '''Method that returns the first_name plus the last_name, with a space in between.'''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def full_name_and_email(self):
        '''Method that returns the first_name plus the last_name, with a space in between.'''
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.email)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''Method that sends an email to the user.'''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def active(self):
        '''Is the user active and have portal access?'''
        return self.is_active

    @property
    def staff(self):
        '''Is the user staff?'''
        return self.is_staff

    @property
    def superuser(self):
        '''Is the user a superuser? Simplest possible answer: All admins are staff.'''
        return self.is_superuser

    def __str__(self):
        '''Method that returns unique user identifier based on email and full name.'''
        '''i.e: return self.first_name + " " + self.last_name + " - Email: " + self.email'''
        return self.full_name_and_email()
