from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileManager(models.Manager):
    def create_Profile(self, User,profilePic):
        profile = self.create(User=User, profilePic=profilePic)
        profile.save()
        return profile

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.ImageField(null=True, upload_to='media')
    objects = ProfileManager()
    
    def __String__(self):
        return self



