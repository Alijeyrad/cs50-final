from django.db import models
from panel.models import User

# Create your models here.

class Advice(models.Model):
    doctor = models.ForeignKey(User, related_name="advice_giver", on_delete=models.CASCADE)
    test_owner = models.ForeignKey(User, related_name="test_owner", on_delete=models.CASCADE)
    test_id = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.username}'s advice for {self.test_owner.username}"