from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Users import views

app_name = 'profile_settings'

urlpatterns = [ 
    path('Signup/', views.signup, name='signup_page'),
    path('Profile/', views.displayProfile, name='profile_page'),
    path('Account/', views.accountSettings, name='account_settings'),
    path('DeleteAccount/<int:pk>/', views.deleteAccount, name='delete_user'),
    path('UpdateAvatar/', views.changeAvatar, name='change_avatar')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)