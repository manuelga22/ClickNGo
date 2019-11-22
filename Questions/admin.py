from django.contrib import admin
from .models import Question, Response
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('User', 'Question', 'Description')
admin.site.register(Question, QuestionAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('Question', 'User', 'Response')
admin.site.register(Response, ResponseAdmin)    
