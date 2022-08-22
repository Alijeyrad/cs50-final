from django.db import models
from panel.models import User

# Create your models here.

class Result(models.Model):
    test_id = models.CharField(max_length=255)
    receiver_doctor = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    sender_user = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)