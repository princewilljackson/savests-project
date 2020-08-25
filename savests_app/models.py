from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """Creates a user profile table in database."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


class Mail(models.Model):
    

    class Meta:
        verbose_name = "Email User"
        verbose_name_plural = "Email Users"

class MailText(models.Model):
    subject = models.Charfield()
    message = models.Charfield()
    users = models.ManyToManyField(Mail)
    send_it = models.BooleanField(default=False) #check it if you want to send your email

    def save(self):
        if self.send_it:
            #First you create your list of users
            user_list = []
            for u in self.users:
                user_list.append(u.email)

            #Then you can send the message. 
            send_mail(str(self.subject), 
                        str(self.message),
                        'from@example.com',
                        user_list, 
                        fail_silently=False)

    class Meta:
        verbose_name = "Emails to send"
        verbose_name_plural = "Emails to send"
