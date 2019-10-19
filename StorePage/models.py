from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  User = models.OneToOneField(User,on_delete=models.CASCADE),
  username = models.CharField(max_length=20),
  password = models.CharField(max_length=20),

def __String__(self):
  return self

