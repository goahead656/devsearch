from django.shortcuts import render, redirect
from django.http import HttpResponse
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
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/create-project.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    # instance is necessary,be carefully
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "projects/delete-project.html", context)
