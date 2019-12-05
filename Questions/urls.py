from django.urls import path
from .views import HomePageView, SearchResultsView
from . import views

app_name = 'Question'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('createQuestion/', views.createQuestion, name='createQuestion'),
    path('questions/', views.allQuestions, name='allQuestions'),
    path('<str:title>', views.questionDetail, name='questionDetail'),
    path('<str:title>/<int:pk>',views.editReply, name="update_reply"),
]