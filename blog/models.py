from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=400, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
