from django.shortcuts import render
from .forms import SignupForm
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 

# Create your views here.
