from django.db.models import fields
from django.forms import ModelForm
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']