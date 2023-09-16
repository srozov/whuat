from django import forms
from django.contrib.auth.models import User

from profiles.models import UserProfile


class SimpleSignUpForm(forms.ModelForm):

    username = forms.CharField(
        max_length=16,
        help_text='',
        validators=[]
    )

    class Meta:
        model = User
        fields = ['username']

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user_profile = UserProfile(number_of_answered_questions=0)
    #
    #     if commit:
    #         user.save()
    #         user_profile.user = user
    #         user_profile.save()
    #
    #     return user, user_profile