from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import UserProfile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create User
            user_profile = UserProfile.objects.create(
                user=user,
                number_of_answered_questions=0,
            )  # Create UserProfile

            # You can add a success message or redirect the user to a login page here.
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})