from projectapp.forms import ProjectCreationForm
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from projectapp.models import Project
# Create your views here.


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self) -> str:
        return reverse("projectapp:detail", kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "target_project"
    template_name = "projectapp/detail.html"


class ProjectListView(ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "projectapp/list.html"
    paginate_by = 7
