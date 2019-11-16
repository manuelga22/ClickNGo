from django.urls import path
from . import views

app_name = 'Communities'

urlpatterns = [
    path('', views.AllCommunities, name='all_communities'),
    path('<str:community_name>/', views.CommunityInfo, name='CommunityInfo'),
]