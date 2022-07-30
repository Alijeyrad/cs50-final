from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    home_town = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, default='/empty-profile.png', upload_to='profile_pics')