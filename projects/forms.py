from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # control the attribute of the model displayed
        fields = [
            "title",
            "description",
            "featured_image",
            "demo_link",
            "source_link",
            "tags",
        ]
