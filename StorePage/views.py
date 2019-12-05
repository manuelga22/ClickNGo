from django.shortcuts import render
from django.contrib.auth.models import User
from Users.models import Profile 
# Create your views here.
def index(request):
  if request.user.is_authenticated:
    profile = Profile.objects.get(User=request.user)
    return render(request, 'StorePage/home_page.html', {'profile':profile})

  return render(request, 'StorePage/home_page.html', {})
