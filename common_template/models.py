from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default='', blank=True)
    views = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

