from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Egg(models.Model):
    dob = models.DateTimeField(default=timezone.now)
    health = models.FloatField(default=1.0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    def age_in_seconds(self):
        now = timezone.now()
        age_timedelta = now - self.dob
        return age_timedelta.total_seconds()

class Question(models.Model):

    question_text = models.TextField()
    previous_question = models.OneToOneField(
        'self', null=True, blank=True, related_name='next_question', on_delete=models.SET_NULL
    )

class Answer(models.Model):

        ANSWER_CHOICES = (
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        )

        choice = models.CharField(max_length=10, choices=ANSWER_CHOICES)
        answer_text = models.TextField()
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
