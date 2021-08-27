from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='roject/', null=False)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pk} : {self.title}'
