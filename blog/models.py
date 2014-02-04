from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=400, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


    def wikitext(self):
        lines = self.content.splitlines()
        s = "".join(["<li>{}</li>".format(escape(line)) for line in lines])
        return mark_safe("<ul>{}</ul>".format(s))

    def get_absolute_url(self):
        if self.slug:
            return reverse('post_by_slug', args=(
                self.slug,
            ))
        return reverse('post', args=(
            self.id,
        ))
