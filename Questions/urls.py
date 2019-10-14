from django.urls import path
from .views import HomePageView, SearchResultsView


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('createQuestion/', views.createQuestion, name='createQuestion'),
]