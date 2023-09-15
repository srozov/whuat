from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # Add other URL patterns as needed
]