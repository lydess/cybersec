from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from users.models import CustomUser


class ContactMessage(models.Model):
    TOPIC = (
        ('a', 'Enquiries'),
        ('b', 'Comments'),
        ('c', 'Site Bugs'),
        )

    contact = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    contact_email = models.EmailField(('Contact Email'),
        help_text='Please enter a valid email address.' ,
        unique=False) #, default=get_user_model().email  # , help_text='Please enter a valid email address.'
    contact_first_name = models.CharField(('First Name'),
        help_text='That being other than the others.',
        max_length=60) #,default=get_user_model().first_name
    contact_last_name = models.CharField(('Last Name'), max_length=60) #, default=get_user_model().last_name
    topic = models.CharField(('Topic'), max_length=12, choices=TOPIC, default='a')
    subject = models.CharField(('Subject'), max_length=60, blank=False)
    message = models.TextField(('Message'), blank=False)
    message_date = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'contact_email'
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact_email', 'contact_first_name', 'contact_last_name', 'topic', 'subject' 'message', ]

    class Meta:
        ''' Class to support search functions.'''
        ordering = ["message_date"]
        verbose_name = _('contact_message')
        verbose_name_plural = _('contacts_messages')

    def contact_tag(self):
        ## Method that returns the message_date and the message subject, with a space in between.
        contact_tag = '%s %s' % (self.message_date, self.subject)
        return contact_tag.strip()

    def __str__(self):
        return self.id()
# Create your models here.
