from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project
# Create your models here.


class Subscribe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subcribe')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='subcribe')

    class Meta:
        unique_together = ('user', 'project')
