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
