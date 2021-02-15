from django.contrib import admin
from .models import Question
from .models import Answer


# Searching data at django admin page
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question, QuestionAdmin)

# Searching data at django admin page
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Answer, AnswerAdmin)
