from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return '{0}'.format(self.tag)

class Bookmark(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    url = models.URLField(max_length=200, blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=True,)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.title)