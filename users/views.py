from django.shortcuts import render
from .models import Profiles

# Create your views here.


def profiles(request):
    profiles = Profiles.objects.all()
    context = {"profiles":profiles}
    return render(request, "users/profiles.html",context)

def userProfile(request,pk):
    profile = Profiles.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile,"topSkills":topSkills,"otherSkills":otherSkills}
    return render(request,"users/user-profile.html",context)
