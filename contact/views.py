# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
# contact/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactMessageForm, AuthContactMessageForm


def contact(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = AuthContactMessageForm()

        else:
            form = ContactMessageForm()

    else:
        if request.user.is_authenticated:
            form = AuthContactMessageForm(request.POST)
            if form.is_valid():
                human = True

                topic = form.cleaned_data['topic']

                if topic is 'a':
                    topic_name = 'EQUIRIES: '
                elif topic is 'b':
                    topic_name = 'COMMENTS: '
                elif topic is 'c':
                    topic_name = 'BUGS: '
                else:
                    topic_name = 'NO TOPIC SELECTED: '

                contact_email = request.user.email
                contact_first_name = request.user.first_name
                contact_last_name = request.user.last_name

                contact_name = contact_first_name + ' ' + contact_last_name
                name_sent = "Contact Name: " + contact_name
                email_sent = "Contact Email: " + contact_email
                details_sent = name_sent +'\n'+ email_sent
                subject = topic_name + form.cleaned_data['subject']
                message = "Message: " +'\n'+ form.cleaned_data['message'] +'\n'+ details_sent
                from_email = 'backend@domain.org'
                fail_silent = False

                if topic is 'a':
                    recipient_list = ['enquires@domain.tld']
                elif topic is 'b':
                    recipient_list = ['feedback@domain.tld']
                elif topic is 'c':
                    recipient_list = ['web@domain.tld']
                else:
                    recipient_list = ['web@domain.tld']

                try:
                    send_mail(subject, message, from_email, recipient_list, fail_silent)

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return redirect('success')

            else:
                form = AuthContactMessageForm()

        else:
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                human = True

                topic = form.cleaned_data['topic']

                if topic is 'a':
                    topic_name = 'EQUIRIES: '
                elif topic is 'b':
                    topic_name = 'COMMENTS: '
                elif topic is 'c':
                    topic_name = 'BUGS: '
                else:
                    topic_name = 'NO TOPIC SELECTED: '

                contact_email = form.cleaned_data['contact_email']
                contact_first_name = form.cleaned_data['contact_first_name']
                contact_last_name = form.cleaned_data['contact_last_name']

                contact_name = contact_first_name + ' ' + contact_last_name
                name_sent = "Contact Name: " + contact_name
                email_sent = "Contact Email: " + contact_email
                details_sent = name_sent +'\n'+ email_sent
                subject = topic_name + form.cleaned_data['subject']
                message = "Message: " +'\n'+ form.cleaned_data['message'] +'\n'+ details_sent
                from_email = 'backend@domain.org'
                fail_silent = False

                if topic is 'a':
                    recipient_list = ['enquires@domain.tld']
                elif topic is 'b':
                    recipient_list = ['feedback@domain.tld']
                elif topic is 'c':
                    recipient_list = ['web@domain.tld']
                else:
                    recipient_list = ['web@domain.tld']

                try:
                    send_mail(subject, message, from_email, recipient_list, fail_silent)

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return redirect('success')

            else:
                form = ContactMessageForm()

    return render(request, "contact.html", {'form': form})


def success(request):
    return render(request, 'success.html', {})
