from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

# All projects
def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


# Single project
def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    form = ProjectForm(instance=project)
    return render(request, "projects/single-project.html", context)


def projectForm(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/project-form.html", context)


# create a new project
@login_required(login_url="login")
def createProject(request):
    #make sure this profile is this user's profile
    profile = request.user.profiles

    form = ProjectForm()

    if request.method == "POST":
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/create-project.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    #make sure this profile is this user's profile
    profile = request.user.profiles
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    # instance is necessary,be carefully
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    #make sure this profile is this user's profile
    profile = request.user.profiles
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("account")

    context = {"object": project}
    return render(request, "delete_template.html", context)
