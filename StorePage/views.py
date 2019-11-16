from django.shortcuts import render
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import Profile 
=======
>>>>>>> 67b354d9c77c63bd7632717a7be0711a04cc8e07
# Create your views here.
def index(request):
    User = request.user
    return render(request, 'StorePage/home_page.html', {'user':User})
