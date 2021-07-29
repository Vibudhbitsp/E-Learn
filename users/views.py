from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    if (CreatorProfile.objects.filter(creatorusr = request.user).exists() or LearnerProfile.objects.filter(learnerusr = request.user).exists()):
        messages.success(request, 'Welcome Back !')
        return redirect('course')
    else:
        messages.success(request, 'Choose one path below and Register ! ')
        return render(request, 'users/register.html')

def creator_register(request):
    if User.objects.filter(username=request.user).exists():
        if request.method == 'POST':
            form=CreatorRegisterForm(request.POST)

            if form.is_valid():
                form.instance.creatorusr = request.user
                form.save()
                username = form.cleaned_data.get('Name')
                messages.success(request,f'CONGRATS {username} !, Your Creator profile is now created!')
                return redirect("course")
        else:
            form = CreatorRegisterForm()
            
            messages.success(request,f'Please complete the verification below !')
        return render(request, 'users/creator_register.html', {'form':form})
        
    else:
        if request.method == 'POST':
            form = CreatorRegisterForm(request.POST)
            form_user = UserRegisterForm(request.POST)
            if form.is_valid():
                if form_user.is_valid():
                    user = form_user.save()
                    
                    creator_profile = form.save(commit=False)
                    creator_profile.creatorusr = user
                    creator_profile.save()
                    messages.success(request, f'Your account has been created! You are now able to log in')
                    return redirect('login')
        else:
            form = CreatorRegisterForm()
            form_user = UserRegisterForm()
        
        return render(request, 'users/creator_register.html', {'form': form , 'form_user' : form_user })

def learner_register(request):
    if User.objects.filter(username=request.user).exists():
        if request.method == 'POST':
            form=LearnerRegisterForm(request.POST)

            if form.is_valid():
                form.instance.learnerusr = request.user
                form.save()
                username = form.cleaned_data.get('Name')
                messages.success(request,f'CONGRATS {username} !, Your Learner profile is now created!')
                return redirect("course")
        else:
            form = LearnerRegisterForm()
            
            messages.success(request,f'Please complete the verification below !')
        return render(request, 'users/learner_register.html', {'form':form})
    
    else:
        if request.method == 'POST':
            form = LearnerRegisterForm(request.POST)
            form_user = UserRegisterForm(request.POST)
            if form.is_valid():
                if form_user.is_valid():
                    user = form_user.save()
                    
                    learner_profile = form.save(commit=False)
                    learner_profile.learnerusr = user
                    learner_profile.save()
                    
                    messages.success(request, f'Your account has been created! You are now able to log in')
                    return redirect('login')
        else:
            form = LearnerRegisterForm()
            form_user = UserRegisterForm()
        return render(request, 'users/learner_register.html', {'form': form , 'form_user' : form_user })


@login_required
def profile(request):
    return render(request, 'users/profile.html')


