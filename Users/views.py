from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUpForm, UsernameChangeForm, ProfileCreateForm, UploadFileForm, EnterEmailForm,ResetPasswordForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from Questions.models import Question
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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
    except:
      messages.warning(request, "Couldn't find an user with those credentials")
      return HttpResponseRedirect(request.path_info)
    return redirect('/')
  else:
    form=  EnterEmailForm()
    return render(request, 'Users/forgotPassword.html', {'form': form}) 

def resetPassword(request,pk):
    if request.method == "POST":
       userObj = User.objects.get(pk=pk)
       form= ResetPasswordForm(request.POST, instance= userObj)
       if form.data['password']==form.data['passwordCheck']:#check if passwords matched
        if form.is_valid():
           if(len(form.data['password']) >8 and not(form.data['password'].isdigit())  ):#conditions for the new passwords
              form.save()
              userObj.set_password(form.data['password'])
              userObj.save()
              messages.success(request,"changed password succesfully")
              return redirect('/login')
           else:
              messages.warning(request," Make sure your password contains more than 9 characters and is not only numbers")
              return HttpResponseRedirect(request.path_info)
       else:#if passwords didn't match
         messages.warning(request, "Passwords don't match")
         return HttpResponseRedirect(request.path_info)
    else:
       userObj = User.objects.get(pk=pk)
       form= ResetPasswordForm()
       return render(request, 'Users/resetPassword.html', {'form': form,'user':userObj}) 



# Profile Page
@login_required
def displayProfile(request):
    profile = Profile.objects.get(User = request.user)
    UserQuestions = Question.objects.get(User=profile)
    # userQuestions = get_object_or_404(Question, User = User_id)
    return render(request, 'Users/Question.html', {
      'profile': profile,
      'questions': UserQuestions.Question, 
    })



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
          print("yooo2>>>>>>>")
          messages.success(request, 'Profile picture has been updated!')
          return redirect('/Account/')
       else:
          messages.warning(request, 'Could not update profile')
          return HttpResponseRedirect(request.path_info)
        
          
  

    

 




