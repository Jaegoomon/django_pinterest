from django.db import models
from articleapp.models import Article
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, related_name='comment', null=True)
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='comment', null=True)

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
