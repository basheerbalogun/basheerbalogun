
from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInLine(admin.StackedInline):# admin.TabularInLine to see it in tabular format
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {"fields":['question_text']}),
        ('Date information',{'fields': ['pub_date']}),  
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)