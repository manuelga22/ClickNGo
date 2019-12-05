from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Users.models import Profile
from crispy_forms.helper import FormHelper
# User registration form
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=128) # Added email field
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["User", "profilePic"]

class UploadFileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=["profilePic"]

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class EnterEmailForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username','email']
        

class ResetPasswordForm(forms.ModelForm):
    passwordCheck = forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=['password','passwordCheck']






