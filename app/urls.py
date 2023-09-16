from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_random_question/', views.get_random_question, name='get_random_question'),
    path('submit_selected_answer/', views.submit_selected_answer, name='submit_selected_answer'),
    path('get_valuable_insights/', views.get_valuable_insights, name='get_valuable_insights'),
    path('state/', views.state, name='state'),
]
