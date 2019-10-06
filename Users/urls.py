<<<<<<< HEAD
from django.urls import pathfrom
import . from views

urlpatterns = [
  path('/login',views.login)
=======
from django.urls import path
from . import views

app_name = 'profile_settings'

urlpatterns = [ 
    path('Signup/', views.signup, name='signup_page'),
    path('Profile/', views.displayProfile, name='profile_page'),
    path('Account/', views.accountSettings, name='account_settings')
>>>>>>> b2de61dc1213f4aa763dcfeeac02dbd2ffcb482c
]