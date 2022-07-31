from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='/empty-profile.png', upload_to='profile_pics')
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    last_profile_update = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=100, blank=True, null=True)
    