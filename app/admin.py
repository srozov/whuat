from django.contrib import admin

from .models import Egg, Question, Answer, SelectedAnswer

@admin.register(Egg)
class EggAdmin(admin.ModelAdmin):
    list_display = ('dob', 'health', 'age_in_seconds')
    # list_filter = ('health',)
    readonly_fields = ['health', 'active_multiplier']
    search_fields = ('dob',)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    readonly_fields = ['selected_answer_count']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'previous_question')
    list_filter = ('previous_question',)
    search_fields = ('question_text',)
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('choice', 'answer_text', 'question')
    list_filter = ('question',)
    search_fields = ('answer_text',)

@admin.register(SelectedAnswer)
class SelectedAnswerAdmin(admin.ModelAdmin):
    list_display = ('choice', 'question', 'userprofile')
    list_filter = ('question',)
    search_fields = ('choice', 'question__question_text')
