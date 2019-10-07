from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UsernameChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile 


from django.contrib.auth.models import User;


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login') 
    else:
        form = UserSignUpForm()
    return render(request, 'Users/signup.html', {'form': form})

# Profile Page
@login_required
def displayProfile(request):
    return render(request, 'Users/profile.html', {})


@login_required 
def accountSettings(request):
    if request.method == 'POST':
        username_form = UsernameChangeForm(request.POST, instance=request.user)
        if username_form.is_valid(): #FIXME: Check username is already taken first before saving
            username_form.save() 
            return HttpResponseRedirect(request.path_info)
    else:
        username_form = UsernameChangeForm(instance=request.user)
        return render(request, 'Users/accountSettings.html', {'username_form': username_form})


@login_required
def deleteAccount(request,pk):
    userObj=User.objects.get(pk=pk)
    userObj.delete()
    return redirect('/')
       


