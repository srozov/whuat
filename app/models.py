from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Egg(models.Model):
    CRACKING_MULTIPLIER = (0.3, 'cracking multiplier')
    MAX_CRACKING_COMMUNITY_MULTIPLIER = (0.5, 'MAX-CRACKING COMMUNITY MULTIPLIER')

    dob = models.DateTimeField(default=timezone.now)
    # health = models.FloatField(default=1.0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    MAX_ANSWERS = 100

    def health(self):
        return max(1.0 - SelectedAnswer.objects.count() / self.MAX_ANSWERS, 0.0)

    def active_multiplier(self):
        if self.health() < 1 - self.MAX_CRACKING_COMMUNITY_MULTIPLIER[0]:
            return self.MAX_CRACKING_COMMUNITY_MULTIPLIER[1]

        elif self.health() < 1 - self.CRACKING_MULTIPLIER[0]:
            return self.CRACKING_MULTIPLIER[1]

        else:
            return


    def age_in_seconds(self):
        now = timezone.now()
        age_timedelta = now - self.dob
        return age_timedelta.total_seconds()

class Question(models.Model):

    question_text = models.TextField()
    themes = models.TextField()

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

    def selected_answer_count(self):
        # Calculate the count of related SelectedAnswer instances for this Answer
        return SelectedAnswer.objects.filter(question=self.question, choice=self.choice).count()


class SelectedAnswer(models.Model):

    userprofile = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE)
    choice = models.CharField(max_length=10, choices=Answer.ANSWER_CHOICES)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


