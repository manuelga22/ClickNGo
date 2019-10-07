from django import forms
from django.forms import ModelForm

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question 
        fields = 