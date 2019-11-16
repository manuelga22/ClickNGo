from django.shortcuts import render, redirect, get_object_or_404
from .models import Community

# Create your views here.
def AllCommunities(request):
    Communities = Community.objects.all() # Get all communities
    return render(request, 'Communities/Community_list.html', {'Community': Communities})

def CommunityInfo(request, community_name):
    community = get_object_or_404(Community, Name=community_name) # Get community based on name
    return render(request, 'Communities/Community_info.html', {'Community': community})
