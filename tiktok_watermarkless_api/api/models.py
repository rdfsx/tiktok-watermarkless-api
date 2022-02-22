import uuid

from django.db import models


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=150, default=None)

    class Meta:
        ordering = ['created']


class MediaResult(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    link = models.URLField(max_length=200, min_length=None, allow_blank=False)

    class Meta:
        managed = False
