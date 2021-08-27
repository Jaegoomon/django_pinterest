from re import template
from articleapp.models import Article
from projectapp.models import Project
from typing import Any
from django.contrib.auth import login
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import RedirectView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from subscribeapp.models import Subscribe

# Create your views here.


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args: Any, **kwargs: Any):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:

        project = get_object_or_404(
            Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscribe.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscribe(user=user, project=project).save()

        return super().get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscribe.objects.filter(
            user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list
