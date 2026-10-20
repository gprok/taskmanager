from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Task(models.Model):
    content = models.CharField(max_length=250, null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.content
