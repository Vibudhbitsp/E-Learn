from django import forms
from django.db import models
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= [ 'username','password1','password2']

class CreatorRegisterForm(forms.ModelForm):
    class Meta:
        model = CreatorProfile
        fields = [
            'Name',
            'Email',
            'Date_Of_Birth',
            'City',
            'State',
            'Educational_Qualification'
        ]

class LearnerRegisterForm(forms.ModelForm):
    class Meta:
        model = LearnerProfile
        fields = [
            'Name',
            'Email',
            'Date_Of_Birth',
            'City',
            'State'
        ]

