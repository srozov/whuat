from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_answered_questions')  # Use the custom method 'display_answered_questions'
    list_filter = ('user__is_active',)  # Add filters for the list view
    search_fields = ('user__username',)  # Add a search field

    def display_answered_questions(self, obj):
        return ', '.join([str(question) for question in obj.answered_questions.all()])

    display_answered_questions.short_description = 'Answered Questions'

admin.site.register(UserProfile, UserProfileAdmin)
