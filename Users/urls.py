from django.urls import pathfrom
import . from views

urlpatterns = [
  path('/login',views.login)
]