from django.db import models
from django.utils.timezone import now
from django.core.validators import EmailValidator

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} By {self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'