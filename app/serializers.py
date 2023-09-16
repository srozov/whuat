from rest_framework import serializers
from .models import (
    Answer, SelectedAnswer, Question
)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text',)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('choice', 'answer_text')


class SelectedAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedAnswer
        fields = ('question', 'choice')