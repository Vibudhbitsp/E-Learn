from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class CreatorProfile(models.Model):
    creatorusr = models.OneToOneField(User, on_delete = models.CASCADE)

    Name = models.CharField(max_length = 200)
    Email = models.EmailField(max_length = 200)
    Date_Of_Birth = models.DateField(default = None)
    City = models.CharField(max_length = 200)
    State = models.CharField(max_length = 200)
    Date_Of_Joining = models.DateField(auto_now = True)
    Educational_Qualification = models.CharField(max_length = 200)
    rating = models.FloatField(default = 3)

    def __str__(self):
        return f'{self.creatorusr.username} CreatorProfile'
    

class LearnerProfile(models.Model):
    learnerusr = models.OneToOneField(User, on_delete = models.CASCADE)
    Name = models.CharField(max_length = 200)
    Email = models.EmailField(max_length = 200)
    Date_Of_Birth = models.DateField(default = None)
    City = models.CharField(max_length = 200)
    State = models.CharField(max_length = 200)
    Date_Of_Joining = models.DateField(auto_now = True)

    def __str__(self):
        return f'{self.learnerusr.username} LearnerProfile'

