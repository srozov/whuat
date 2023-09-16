from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import *
from profiles.models import UserProfile
from prompts.src.sustainability_profile import create_user_profile


@api_view(['GET'])
def get_valuable_insights(request):

    payload = []

    user_profile = request.user.userprofile
    for q in user_profile.answered_questions.all():
        choice = SelectedAnswer.objects.get(question=q, userprofile=request.user.userprofile).choice
        answer_text = q.answer_set.get(choice=choice).answer_text
        # answer_text = Answer.objects.get(question=q, choice=choice).answer_text
        alternatives = list(q.answer_set.exclude(choice=choice).values_list('answer_text', flat=True))
        row = {
            'question': q.question_text,
            'selected_answer': answer_text,
            'alternatives': alternatives,
        }

        payload.append(row)

    response = create_user_profile(payload)

    # return JsonResponse(payload, safe=False)
    return JsonResponse({'response': response}, safe=False)



@api_view(['GET'])
def get_random_question(request):
    # Fetch a random question which hasn't yet been answered by the user
    user_profile = request.user.userprofile
    random_question = Question.objects.exclude(
        id__in=user_profile.answered_questions.values_list('id', flat=True)
    ).order_by('?').first()

    if random_question:
        # Serialize the answers
        answers = AnswerSerializer(random_question.answer_set.all(), many=True).data

        # Create the response data
        data = {
            'question': QuestionSerializer(random_question).data,
            'answers': {item['choice']: item['answer_text'] for item in answers},
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'No questions available.'}, status=404)

@api_view(['POST'])
def submit_selected_answer(request):
    data = {
        **request.data,
        'userprofile': request.user.userprofile.pk,
    }
    serializer = SelectedAnswerSerializer(data=data)

    if serializer.is_valid():
        # Save the submitted SelectedAnswer
        serializer.save()
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        user_profile.answered_questions.add(serializer.data['question'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def state(request):
    active_users_count = User.objects.filter(is_active=True).count()

    egg, created = Egg.objects.get_or_create()

    data = {
        'active_users_count': active_users_count,
        'health': egg.health,
        'age': egg.age_in_seconds(),
    }

    # Return the data as JSON response
    return JsonResponse(data)

def index(request):
    # TODO: create endpoint & js function to refresh count -> why not use react for that???

    if request.user.is_authenticated:

        active_users_count = User.objects.count()

        context = {
            'active_users_count': active_users_count,
            'username': request.user.username,
            'user_greeting': 'whaddup'
        }


        return render(request, 'index.html', context)

    else:
        # User is not logged in, return a forbidden response or redirect to login
        return redirect('accounts/signup/')  # Redirect to the login page or another appropriate page
