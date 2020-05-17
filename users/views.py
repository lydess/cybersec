# -*- coding: utf-8 -*-
# users/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .models import CustomUser
from .forms import CustomUserCreationForm
from .tokens import account_activation_token


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            applicant = form.save(commit=False)
            applicant.is_active = False
            applicant.save()

            current_site = get_current_site(request)
            email_subject = 'Activate your account'
            message = render_to_string('activate_account.html', {
                'user': applicant,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(applicant.pk)),
                'token': account_activation_token.make_token(applicant),
            })

            send_to_email = form.cleaned_data.get('email')
            activation_email = EmailMessage(email_subject, message, to=[send_to_email])
            activation_email.send()
            return render(request, 'activation_sent.html', {})

    else:
        form = CustomUserCreationForm()

    return render(request, "signup.html", {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        applicant = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        applicant = None
    if applicant is not None and account_activation_token.check_token(applicant, token):
        applicant.is_active = True
        applicant.save()
        login(request, applicant)
        return render(request, 'activation_success.html', {})
    else:
        return render(request, 'activation_invalid.html', {})


def activation_sent(request):
    return render(request, 'activation_sent.html', {})


def activation_success(request):
    return render(request, 'activation_success.html', {})


def activation_invalid(request):
    return render(request, 'activation_invalid.html', {})

