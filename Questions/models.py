from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Question = models.CharField(max_length=256)
    Description = models.CharField(max_length=10000)
    
    class Meta:
      verbose_name_plural = "Questions"

    def __str__(self):
        return self.Title