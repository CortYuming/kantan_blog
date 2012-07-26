from django.db import models
from django.core.urlresolvers import reverse


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
