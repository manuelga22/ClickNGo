from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignUpForm, UsernameChangeForm, ProfileCreateForm, UploadFileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile 

from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        newUser = UserSignUpForm(request.POST)
        if newUser.is_valid():
            newUser.save()
            user = User.objects.get(username = newUser.cleaned_data['username'])  #get instance to save a profile
            Profile.objects.create_Profile(user, '/defaultAvatar.png')
            return redirect ('login') 
    else:
        form = UserSignUpForm()
        return render(request, 'Users/signup.html', {'form': form})

# Profile Page
@login_required
def displayProfile(request):
    profile = Profile.objects.get(User = request.user)
    return render(request, 'Users/profile.html', {'profile': profile})


@login_required 
def accountSettings(request):
    if request.method == 'POST':
        print('updating>>>>>>>>>>')
        username_form = UsernameChangeForm(request.POST, instance=request.user)
        if username_form.is_valid(): #FIXME: Check username is already taken first before saving
            username_form.save() 
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
    return redirect('/')

@login_required
def changeAvatar(request, template_name="Users/accountSettings.html"):
      print("yooo>>>>>>>")
      if request.method == 'POST':
       profileObj = Profile.objects.get(User= request.user)
       form =  UploadFileForm(request.POST or None, request.FILES or None, instance=profileObj)
       if form.is_valid():
          form.save()
          print("yooo2>>>>>>>")
          return redirect('/Account/')
        
          
  

    

 




