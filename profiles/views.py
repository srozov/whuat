from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect

from .forms import SimpleSignUpForm
from .models import UserProfile


def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SimpleSignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']

            # Check if a user with the same username already exists
            if not User.objects.filter(username=username).exists():
                # Create a User instance
                user = User.objects.create_user(username=username)
                user_profile = UserProfile.objects.create(
                    user=user,
                    number_of_answered_questions=0,
                )

                login(request, user)

                return redirect('/')  # Redirect to the login page or another appropriate page

            # Handle the case where the username is already taken
            else:
                form.add_error('username', 'This username is already taken.')

            return redirect('/')
    else:
        form = SimpleSignUpForm()

    return render(request, 'signup.html', {'form': form})