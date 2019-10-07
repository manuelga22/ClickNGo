from django.db import models
from django.contrib.auth.models import User
#from PIL import Image FIXME: Add profile picutres

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    #picture = models.ImageField()
    
    def __String__(self):
        return self


