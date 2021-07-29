from users.models import LearnerProfile
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_content = models.TextField()
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateField(auto_now=True)
    Course_Tag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        
        return reverse ('course-detail',kwargs = {'pk': self.pk})
        
class Modules(models.Model):
    Title = models.CharField(max_length=100)
    content = models.TextField()
    index = models.IntegerField(default=1)
    Course = models.ForeignKey(Courses, on_delete = models.CASCADE)
    link = models.URLField()

    def save(self,**kwargs):
        current_module = Modules.objects.filter(id = self.pkk)
        all_modules = Modules.objects.filter(Course = current_module.Course)
        current_module.index = all_modules.count + 1
        return super(Modules,self).save(**kwargs)
    def __str__(self):
        return self.Title

    def get_absolute_url(self,):
        
        return reverse ('module-detail',kwargs = {'pk':self.Course.pk , 'pkk': self.pk })


class Classroom(models.Model):
    learners = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'classes')
    courses = models.ForeignKey(Courses, on_delete = models.CASCADE, related_name = 'classrooms')
    Course_completed = models.BooleanField(default = False)

class ClassroomModules(models.Model):
    learners = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'classesmodules')
    modules = models.ForeignKey(Modules, on_delete = models.CASCADE, related_name = 'classrooms')
    completed = models.BooleanField(default = False)


class ReviewCourse(models.Model):
    learner = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.TextField()
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.review