from django import forms
from django.forms import ModelForm
from .models import Question, Response
from djrichtextfield.widgets import RichTextWidget

maxChar = 10000
class CreateQuestionForm(forms.ModelForm):
    Description = forms.CharField(max_length= maxChar, widget=forms.Textarea(attrs ={'placeholder': 'Max characters is 10000', 'cols': 65, 'rows': 5}))
    class Meta:
        model = Question 
        fields = ['Question', 'Description']

class CreateResponseForm(forms.ModelForm):
    Response = forms.CharField(max_length= maxChar, widget= forms.Textarea(attrs={'placeholder': 'Max characters is 10000', 'cols': 65, 'rows': 5}))
    class Meta:
        model = Response
        fields = ['Response']
