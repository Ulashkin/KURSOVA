from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, ProjectForm
from .models import Project

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('projects_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects_list.html', {'projects': projects})

def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {'form': form})

