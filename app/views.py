import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
from django.views.decorators.http import require_http_methods


from app.models import *
from app.serializers import *
from profiles.models import UserProfile
from prompts.src.sustainability_profile import create_user_profile


def compile_answer_history_payload(request):

    payload = []

    user_profile = request.user.userprofile
    for q in user_profile.answered_questions.all():
        choice = SelectedAnswer.objects.filter(question=q, userprofile=request.user.userprofile).first().choice
        answer_text = q.answer_set.get(choice=choice).answer_text
        # answer_text = Answer.objects.get(question=q, choice=choice).answer_text
        alternatives = list(q.answer_set.exclude(choice=choice).values_list('answer_text', flat=True))
        row = {
            'question': q.question_text,
            'selected_answer': answer_text,
            'alternatives': alternatives,
        }

        payload.append(row)
    return payload


@api_view(['GET'])
def get_valuable_insights(request):

    payload = compile_answer_history_payload(request)
    response = create_user_profile(payload)

    # return JsonResponse(payload, safe=False)
    return JsonResponse({'response': response}, safe=False)


def generate_reward():
    prob = 0.12

    REWARDS = [
        "🎉", "🌟", "🎁", "🥇", "👏", "🍕", "🍦", "🍭", "💎", "🚀", "🌈",
        "❤️", "🔥", "🍔", "🍺", "🏆", "🎈", "📚", "🎮", "💰", "👑", "🎂",
        "🌺", "🍩", "🍓", "🍸", "🎵", "🚲", "🌄", "🏖️", "🚁", "🛋️", "🌆",
        "🌷", "🏀", "🍀", "🎣", "🎤", "🚗", "🌅", "🏕️", "🚢", "🚀", "🎨",
        "🌻", "⚽", "🌊", "🏹", "🎸", "🚁", "🌇", "🏞️", "🛶", "🛰️", "🎭",
        "🌹", "🏈", "🏝️", "🏄", "🎷", "🚆", "🌉", "🏔️", "🛵", "🚤", "🎪"
    ]

    if random.random() <= prob:
        return random.choice(REWARDS)
    else:
        return None  # No reward this time

def get_random_question(request):
    egg, created = Egg.objects.get_or_create()

    egg_health = egg.health()
    if not egg_health:
        data = {"new_url": "/results/"}
        return JsonResponse(data)

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
            'reward': generate_reward()
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

    # egg_health = egg.health()
    # if not egg_health:
    #     data = {"new_url": "/results/"}
    #     return JsonResponse(data)

    data = {
        'active_users_count': active_users_count,
        'health': egg.health(),
        'age': egg.age_in_seconds(),
        'active_multiplier': egg.active_multiplier(),
    }

    # Return the data as JSON response
    return JsonResponse(data)

@require_http_methods(["GET"])
def results(request):

    # userprofile = request.user.userprofile
    #
    # profile_insights = {
    #     'scores' : json.loads(userprofile.scores),
    #     'profile': json.loads(userprofile.profile_text),
    # }

    active_users_count = User.objects.count()
    egg, created = Egg.objects.get_or_create()

    # if not egg.cracked:
    #     egg.cracked = True
    #     egg.save()

    payload = compile_answer_history_payload(request)
    profile_insights = create_user_profile(payload)

        # print('got openai payload')
        #
        # userprofile.scores = json.dumps(profile_insights['scores'])
        # j_txt = json.dumps(profile_insights['profile'])
        # print(j_txt)
        #
        # userprofile.profile_text = j_txt
        # userprofile.save()

    context = {
        'age': egg.age_in_seconds(),
        'active_users_count': active_users_count,
        'username': request.user.username,
        'scores': profile_insights['scores'],
        'profile_insights': profile_insights['profile'],
    }

    return render(request, 'results.html', context)


def index(request):
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
