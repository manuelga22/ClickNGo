from django.urls import path
from . import views


urlpatterns = [
    path('createQuestion/', views.createQuestion, name='createQuestion'),
]