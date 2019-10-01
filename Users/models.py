from django.db import models
from django.contrib.auth.models import User
#from PIL import Image FIXME: Add profile picutres

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    #picture = models.ImageField()

