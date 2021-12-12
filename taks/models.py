from django.contrib.auth import get_user_model
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.TextField(max_length=50)
    address = models.JSONField(blank=True, null=True, default=None)
    phone = models.TextField()
    website = models.URLField()
    company = models.JSONField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class downloader(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.TextField(blank=True, null=True, default=None)
    text = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return self.text

