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
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Doctor(models.Model):
    user = models.ForeignKey(User, related_name='doctor_user', on_delete=models.CASCADE)
    # rating
    CLINICIAN = 'CLI'
    COUNSELOR = 'COU'
    PSYCHIATRIST = 'PST'
    FAMILY = 'MFT'
    SOCIAL = 'SW'
    PSYCHOMETRIST = 'PMT'
    OTHER = 'OTR'
    TITLE = [
        (CLINICIAN, 'Clinical Psychologist'),
        (COUNSELOR, 'Counseling Psychologist'),
        (PSYCHIATRIST, 'Psychiatrist'),
        (FAMILY, 'Marriage And Family Therapist'),
        (SOCIAL, 'Social Worker'),
        (PSYCHOMETRIST, 'Psychometrist'),
        (OTHER, 'Other'),
    ]
    title = models.CharField(
        max_length=3,
        choices=TITLE,
        default=OTHER
    )

    def __str__(self):
        return f"{self.user.username} is a {self.title}"