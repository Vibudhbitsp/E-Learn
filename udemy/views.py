
from django.shortcuts import get_object_or_404,render,redirect,reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
# Create your views here.
from .forms import *
from django.urls import reverse_lazy
from braces import views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect, request
from django.contrib.auth.decorators import login_required, permission_required
from users.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate

def course(request):
    context = {
        'COURSES': Courses.objects.all()
    }
    return render(request, 'udemy/course.html', context)


# class OwnerMixin(object):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(creator=self.request.user)

# class OwnerEditMixin(object):
#     def form_valid(self, form):
#         form.instance.creator = self.request.user
#         return super().form_valid(form)

# class OwnerCourseMixin(OwnerMixin):
    # 
    
class CourseListView(ListView):
    model = Courses
    template_name = 'udemy/course.html'
    context_object_name = 'course'
    ordering = ['-date_posted']


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'udemy/course_detail.html'


class CourseCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    def test_func(self) :
        if CreatorProfile.objects.filter(creatorusr = self.request.user).exists():
            return True
        return False
    model = Courses
    template_name = 'udemy/course_form.html'
    fields = ['course_name','course_content','Course_Tag']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Courses
    fields = ['course_name','course_content']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.creator:
            return True
        return False

def enroll(request, **kwargs):
    coursetoenroll = Courses.objects.filter(id = kwargs['pk'])[0]
    
        
       
    if LearnerProfile.objects.filter(learnerusr = request.user).exists():
        Classroom.objects.create(learners = request.user, courses = coursetoenroll)
        for module in Modules.objects.filter(Course = coursetoenroll):
            ClassroomModules.objects.create(learners = request.user, modules = module)
        messages.success(request, 'Congrats! You have enrolled for the course!')
        return redirect('course-detail', pk = coursetoenroll.id)
    else:
        messages.success(request, 'Being a Creator, You cannot Study Courses !')
        return redirect('course')

def review_course(request,**kwargs):
    coursetoreview = Courses.objects.filter(id = kwargs['pk'])[0]
    if LearnerProfile.objects.filter(learnerusr = request.user).exists():
        if (request.method == 'POST'):
          review_form = ReviewForm(request.POST)
          if review_form.is_valid():
            my_review = review_form.cleaned_data.get('review')
            
            ReviewCourse.objects.create(learner = request.user ,review = my_review , course = coursetoreview)
            return redirect('course')
        else:
          review_form = ReviewForm()
          return render(request,'udemy/review_form.html',{'review_form':review_form})
    else:
        messages.success(request,'you must be a learner to review it')
        return redirect('course')

def showreview(request,**kwargs):
    reviewtoshow = ReviewCourse.objects.filter(course = Courses.objects.filter(id = kwargs['pk'])[0])
    return render(request,'udemy/review.html',{'review':reviewtoshow})

    

@login_required(redirect_field_name = 'register')
def studycourse(request, **kwargs):
    if LearnerProfile.objects.filter(learnerusr = request.user).exists():
        currentcourse = Courses.objects.filter(id = kwargs['pk'])[0]
        if Classroom.objects.filter(learners = request.user, courses = currentcourse).exists():

            mainclass = Classroom.objects.filter(learners = request.user, courses = currentcourse)[0]
            if mainclass.Course_completed == True:
                check = True
            else:
                check = False

            return redirect('course-detail',currentcourse.id)
        else:
            messages.success(request, 'You need to first enroll for the course!')
            return redirect('course')
    else:
        messages.success(request, 'Being a Creator, You cannot Study Courses !')
        return redirect('course')



def module(request):
    context = {
        'MODULE': Modules.objects.all()
    }
    return render(request, 'udemy/module.html', context)

class ModuleListView(ListView):
    
    template_name = 'udemy/module.html'
    model = Modules
    context_object_name = 'module'
    def get_queryset(self,**kwargs):
        course_to_study = Courses.objects.filter(pk = self.kwargs['pk'])[0]
        
        return Modules.objects.filter(Course = course_to_study)
    
    
   

class ModuleDetailView(DetailView):
    model = Modules
    context_object_name = 'module'
    template_name = 'udemy/module_detail.html'
    
    def get_object(self,**kwargs):
        return Modules.objects.filter(id = self.kwargs['pkk'])[0]

    
    
    
    
    
    
     
    
class ModuleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
   
    def test_func(self,**kwargs):
        if self.request.user == Courses.objects.filter(id = self.kwargs['pk'])[0].creator:
          return True
        return False
    model = Modules
    template_name = 'udemy/module_form.html'
    fields = ['Title','content','index','link']
    
    def form_valid(self,form):
        form.instance.creator = self.request.user
        form.instance.Course = Courses.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


    


class ModuleUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Modules
    fields = ['Title','content']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False

def searchbytag(request):
    if request.method == 'POST':
        search_form = SearchByTag(request.POST)

        if search_form.is_valid():
            tag = search_form.cleaned_data.get('tag')
            return render(request, 'udemy/searched.html', {'courses': Courses.objects.filter(Course_Tag__icontains = tag)})

    else:
        search_form = SearchByTag
        totaltags = []
        for course in Courses.objects.all():
            totaltags.append(course.Course_Tag)

        searchedtags = set(totaltags)
        return render(request, 'udemy/searchbytag.html', {'search_form': search_form, 'tags': searchedtags})





def completemodule(request, **kwargs):
    moduletocomplete = Modules.objects.filter(id = kwargs['pkk'])[0]
    classroom = ClassroomModules.objects.filter(learners = request.user, modules = moduletocomplete)[0]
    classroom.completed = True
    classroom.save()
    messages.success(request, 'Congrats! You have Studied the module !')

    number = 0
    for module in Modules.objects.filter(Course = moduletocomplete.Course):
        check = ClassroomModules.objects.filter(learners = request.user, modules = module)[0]
        if check.completed:
            number += 1

    if number == Modules.objects.filter(Course = moduletocomplete.Course):
        messages.success(request, 'Congrats! You have also Completed the Course !!!')
        mainclass = Classroom.objects.filter(learners = request.user, courses = moduletocomplete.Course)[0]
        mainclass.Course_completed = True
        mainclass.save()

        return redirect('review', pk = moduletocomplete.Course.id)

    return redirect('study', pk = moduletocomplete.Course.id)


