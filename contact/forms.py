# -*- coding: utf-8 -*-
# contact/forms.py
from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField

from .models import ContactMessage

class ContactMessageForm(forms.Form):
    TOPIC = (
        ('a', 'Equiries'),
        ('b', 'Comments'),
        ('c', 'Site Bugs'),
        )

    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(help_text='Please enter a valid email address.', required=True)
    topic = forms.ChoiceField(choices=TOPIC)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = CaptchaField()

class ContactMessageForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactMessage
        fields = ('contact_email', 'contact_first_name', 'contact_last_name', 'topic', 'subject', 'message')

class AuthContactMessageForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactMessage
        fields = ('topic', 'subject', 'message')
