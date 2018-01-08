import datetime

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(default=datetime.datetime, blank=True)
    modifiedAt = models.DateTimeField(blank=True, null=True)
