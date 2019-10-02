from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = UserSignUpForm()
    return render(request, 'Users/signup.html', {'form': form})
