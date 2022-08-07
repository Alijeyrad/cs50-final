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

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name="followee", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower} Follows {self.followee}"

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, related_name="comment_writer", on_delete=models.CASCADE)
    for_doctor = models.ForeignKey(User, related_name="comment_for_doctor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.writer} for {self.for_doctor}"

    class Meta:
        ordering = ['-date_posted']

class Star(models.Model):
    voter = models.ForeignKey(User, related_name="voter", on_delete=models.CASCADE)
    
    class StarChoice(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    stars = models.IntegerField(choices=StarChoice.choices)

    is_for = models.ForeignKey(User, related_name="vote_for", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stars} for {self.is_for}"