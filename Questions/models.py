from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=256)
    QuestionField = models.CharField(max_length=10000)