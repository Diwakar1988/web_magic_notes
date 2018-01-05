from django.db import models
from django.db.models import CharField


class User(models.Model):
    email = CharField(max_length=30)
    password = CharField(max_length=30)
    firstName = CharField(max_length=20)
    lastName = CharField(max_length=20)
    gender = CharField(max_length=20)
