from django import forms
from django.db import models
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields=[
            'course_name',
            'course_content',
            'Course_Tag',
        ]

class ModuleCreationForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields =[
            'Title',
            'content',
            'link',
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewCourse
        fields = [
            'review',
        ]


    
class SearchByTag(forms.Form):
    tag = forms.CharField(max_length = 200)