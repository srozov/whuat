from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

from app.models import Question


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question, blank=True)

    profile_text = models.TextField(default='[]')
    scores = models.TextField(default='[]')

    def __str__(self):
        return self.user.username