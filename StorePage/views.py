from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    User = request.user
    return render(request, 'StorePage/home_page.html', {'user':User})
