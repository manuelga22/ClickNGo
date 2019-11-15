from django.shortcuts import render, redirect, get_object_or_404
from .models import Communities

# Create your views here.
def displayAllCommunities(request):
    Community = Communities.objects.get()
    return render(request, 'Communties/AllCommunities.html', {'Community': Community})