from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# User registration form
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=128) # Added email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
