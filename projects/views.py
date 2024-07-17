from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


def project(request):
    return render(request, "projects/single-project.html")


def projectForm(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create-project.html", context)
