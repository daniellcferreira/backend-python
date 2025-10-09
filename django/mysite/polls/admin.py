from django.contrib import admin

from .models import Choice, Question

# Classe de administração para o modelo Choice
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

# Classe de administração para o modelo Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
