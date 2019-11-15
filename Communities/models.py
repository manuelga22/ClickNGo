from django.db import models
from Users.models import Profile
from datetime import datetime   
from django.contrib.auth.models import User

# Create your models here.
class Communities(models.Model):
    #Admin       =         models.ForeignKey(User, on_delete=models.CASCADE, default=)
    Users       =         models.ManyToManyField(Profile) # Users apart of the community
    Name        =         models.CharField(max_length=32, default='None')
    Image       =         models.ImageField(default='community_default.jpg', upload_to='community_pics') # Community image
    Description =         models.TextField(max_length=250, default='None') # Community Description
    Created_on  =         models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.Name
