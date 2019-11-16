from django.db import models
from Users.models import Profile
from datetime import datetime   
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Community(models.Model):
    #Admin       =         models.ForeignKey(User, on_delete=models.CASCADE, default=)
    Users        =         models.ManyToManyField(Profile) # Users apart of the community
    Name         =         models.CharField(max_length=32, default='None')
    Image        =         models.ImageField(default='media/community_pics/defaultAvatar.png', upload_to='community_pics') # Community image
    Description  =         models.TextField(max_length=250, default='None') # Community Description
    Created_on   =         models.DateField(default=datetime.now) # Time Community was created
    
    # Return Community Name
    def __str__(self):
        return self.Name

    # For when a user wants info of a community
    def get_absolute_url(self):
        return reverse('Communities:CommunityInfo', args=[self.Name])
