from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from app.models import *
from app.serializers import *


@api_view(['GET'])
def get_random_question(request):
    # Fetch a random question
    random_question = Question.objects.order_by('?').first()

    if random_question:
        # Serialize the answers
        answers = AnswerSerializer(random_question.answer_set.all(), many=True).data

        # Create the response data
        data = {
            'question': random_question.question_text,
            'answers': {item['choice']: item['answer_text'] for item in answers}
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'No questions available.'}, status=404)


def state(request):
    active_users_count = User.objects.filter(is_active=True).count()

    egg, created = models.Egg.objects.get_or_create()

    data = {
        'active_users_count': active_users_count,
        'health': egg.health,
        'age': egg.age_in_seconds(),
    }

    # Return the data as JSON response
    return JsonResponse(data)

def index(request):
    # TODO: create endpoint & js function to refresh count -> why not use react for that???

    active_users_count = User.objects.count()

    context = {
        'active_users_count': active_users_count,
        'username': request.user.username,
        'user_greeting': 'whaddup'
    }


    return render(request, 'index.html', context)

