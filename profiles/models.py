from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_answered_questions = models.PositiveIntegerField(null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username