from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    url = models.URLField(max_length=200, blank=False, null=False)
    tags = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)