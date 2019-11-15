from django.contrib import admin
#from .models import Question
# Register your models here.
'''
class QuestionAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('User', 'Question', 'Description')
admin.site.register(Question, QuestionAdmin)
'''
=======
    list_display = ['User', 'Question', 'Description']
admin.site.register(Question, QuestionAdmin)
>>>>>>> 755750fc3c28a9549eeae4014ddb8defbd87b7bf
