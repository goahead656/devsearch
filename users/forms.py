from django.forms import ModelForm
from .models import User,Profiles,Skill
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2'
            ]
        labels = {
            'first_name':'Name',
        }

    # change input style
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['name','email','username',
                  'location','bio','short_intro','profile_image',
                  'social_github','social_linkedin','social_twitter',
                  'social_youtube','social_website']
    # change input style
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ['owner']

    # change input style
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


