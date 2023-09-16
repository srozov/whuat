import json

from django.core.management.base import BaseCommand
from app.models import Question, Answer


class Command(BaseCommand):
    help = 'Populate Question and Answer tables from questions.json'

    def handle(self, *args, **kwargs):

        Question.objects.all().delete()
        previous_question = None

        with open('questions.json', 'r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    print(data)

                    question = Question.objects.create(question_text=data['question'], previous_question=previous_question)
                    # Update the previous_question for the next iteration
                    previous_question = question

                    # Create Answer objects
                    for i, answer_text in enumerate(data['answers']):
                        Answer.objects.create(choice=chr(65 + i), answer_text=answer_text, question=question)

                except json.JSONDecodeError as e:
                    # Handle invalid JSON lines if necessary
                    self.stderr.write(f'Error parsing JSON line: {line.strip()}\n{e}')
                    continue
