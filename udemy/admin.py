from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Courses)
admin.site.register(Modules)
admin.site.register(Classroom)
admin.site.register(ClassroomModules)
admin.site.register(ReviewCourse)