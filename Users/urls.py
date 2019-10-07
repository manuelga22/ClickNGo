from django.urls import path
from . import views

app_name = 'profile_settings'

urlpatterns = [ 
    path('Signup/', views.signup, name='signup_page'),
    path('Profile/', views.displayProfile, name='profile_page'),
    path('Account/', views.accountSettings, name='account_settings'),
    path('DeleteAccount/<int:pk>/', views.deleteAccount, name='delete_user')
]