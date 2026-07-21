from django.conf import settings
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=120)
    body = models.TextField()

    def __str__(self):
        return self.title
