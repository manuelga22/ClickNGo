from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Users import views
# social login
from StorePage import views as Storepage_views
from django.conf.urls import url, include
from django.contrib import admin


app_name = 'profile_settings'

urlpatterns = [ 
    path('Signup/', views.signup, name='signup_page'),
    path('Profile/', views.displayProfile, name='profile_page'),
    path('Account/', views.accountSettings, name='account_settings'),
    path('DeleteAccount/<int:pk>/', views.deleteAccount, name='delete_user'),
    path('UpdateAvatar/', views.changeAvatar, name='change_avatar'),

    # social auth
    url('^api/v1/', include('social_django.urls', namespace='social'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)