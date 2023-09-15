from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import UserProfile


class SignUpForm(UserCreationForm):
    # Add any additional fields you want for registration
    class Meta:
        model = User  # Use the built-in User model
        fields = ('username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user_profile = UserProfile(number_of_answered_questions=0)

        if commit:
            user.save()
            user_profile.user = user
            user_profile.save()

        return user, user_profile