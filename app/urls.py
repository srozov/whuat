from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_random_question/', views.get_random_question, name='get_random_question'),
    path('state/', views.state, name='state'),
]
