from django.db import models

# Create your models here.


class Egg(models.Model):
    age = models.IntegerField()
    health = models.FloatField()


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
        question_text = models.TextField()
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
