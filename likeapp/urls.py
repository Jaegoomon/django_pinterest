from likeapp.views import LikeArticleView
from likeapp.models import LikeRecord
from django.urls import path

app_name = 'likeapp'

urlpatterns = [
    path('like/<int:pk>', LikeArticleView.as_view(), name='like'),
]
