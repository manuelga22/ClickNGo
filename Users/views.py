from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUpForm, UsernameChangeForm, ProfileCreateForm, UploadFileForm, EnterEmailForm,ResetPasswordForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile 
from django.core.mail import send_mail
from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        newUser = UserSignUpForm(request.POST)
        if newUser.is_valid():
            newUser.save()
            user = User.objects.get(username = newUser.cleaned_data['username'])  #get instance to save a profile
            Profile.objects.create_Profile(user, '/defaultAvatar.png')
            return redirect ('login') 
        else:
            messages.warning(request, 'Could not create profile')
            return HttpResponseRedirect(request.path_info)
    else:
        form = UserSignUpForm()
        return render(request, 'Users/signup.html', {'form': form})

def changePassword(request):
  if request.method == "POST":
    userForm = EnterEmailForm(request.POST)
    try:
      user = User.objects.get(username = userForm.data['username'], email=userForm.data['email'])
      send_mail(subject="Reset Password", message='Go to this link to reset the password: http://localhost:8000/resetPassword/%s'%user.pk,from_email="sparkdevfiuweb@gmail.com", recipient_list=[user.email],fail_silently=False)
    except user.DoesNotExist:
      messages.warning(request, "Couldn't find an user with those credentials")
    return redirect('/')
  else:
    form=  EnterEmailForm()
    return render(request, 'Users/forgotPassword.html', {'form': form}) 

def resetPassword(request,pk):
    if request.method == "POST":
       userObj = User.objects.get(pk=pk)
       form= ResetPasswordForm(request.POST, instance= userObj)
       if form.data['password']==form.data['passwordCheck']:
        if form.is_valid():
           user = form.save()
           update_session_auth_hash(request, user)
           messages.success(request,"changed password succesfully")
           return redirect('/login')
        else:
           messages.warning(request,"passwords didn't match or couldn't update password")
       else:
           messages.warning(request,"passwords don't match")
       return HttpResponseRedirect(request.path_info)
    else:
       userObj = User.objects.get(pk=pk)
       form= ResetPasswordForm()
       return render(request, 'Users/resetPassword.html', {'form': form,'user':userObj}) 



# Profile Page
@login_required
def displayProfile(request):
    profile = Profile.objects.get(User = request.user)
    return render(request, 'Users/profile.html', {'profile': profile})


@login_required 
def accountSettings(request):
    if request.method == 'POST':
        username_form = UsernameChangeForm(request.POST, instance=request.user)
        if username_form.is_valid(): #FIXME: Check username is already taken first before saving
            username_form.save() 
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'Could not update profile')
            return HttpResponseRedirect(request.path_info)
    else:
        username_form = UsernameChangeForm(instance=request.user)
        profile = Profile.objects.get(User = request.user)
        image_form = UploadFileForm(instance=profile)
        return render(request, 'Users/accountSettings.html', {
            'username_form': username_form,
            'profile':profile,
            'picture_form': image_form
        })


@login_required
def deleteAccount(request,pk):
    userObj=User.objects.get(pk=pk)
    userObj.delete()
    messages.success(request, 'Profile has been deleted. See ya!')
    return redirect('/')
 

@login_required
def changeAvatar(request, template_name="Users/accountSettings.html"):
      if request.method == 'POST':
       profileObj = Profile.objects.get(User= request.user)
       form =  UploadFileForm(request.POST or None, request.FILES or None, instance=profileObj)
       if form.is_valid():
          form.save()
          messages.success(request, 'Profile picture has been updated!')
          return redirect('/Account/')
       else:
          messages.warning(request, 'Could not update profile')
          return HttpResponseRedirect(request.path_info)
        
          
  

    

 




