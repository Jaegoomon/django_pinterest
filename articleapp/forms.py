from projectapp.models import Project
from django import forms
from django.forms import ModelForm, fields
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'editable', 'style': 'height: auto; text-align: left;'}))
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
