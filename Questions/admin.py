from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
<<<<<<< HEAD
    list_display = ('User', 'Question', 'Description')
admin.site.register(Question, QuestionAdmin)
'''
=======
    list_display = ['User', 'Question', 'Description']
admin.site.register(Question, QuestionAdmin)
>>>>>>> 755750fc3c28a9549eeae4014ddb8defbd87b7bf
=======
    list_display = ['User', 'Question', 'Description']
admin.site.register(Question, QuestionAdmin)
>>>>>>> c4aa71058bef52a9bbb55edfe79bec6239f18f5b
