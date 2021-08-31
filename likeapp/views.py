from articleapp.models import Article
from django.contrib import messages
from typing import Any, Optional
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest

from django.http.response import HttpResponse, HttpResponseRedirect
from likeapp.models import LikeRecord
from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> Optional[str]:
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        like_record = LikeRecord.objects.filter(user=user, article=article)

        if like_record.exists():
            messages.add_message(request, messages.ERROR, '좋아요를 취소하였습니다.')

            like_record.delete()
            article.like -= 1
            article.save()
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            messages.add_message(request, messages.SUCCESS, '좋아요를 누르셨습니다.')

            LikeRecord(user=user, article=article).save()
            article.like += 1
            article.save()

        return super(LikeArticleView, self).get(request, *args, **kwargs)
