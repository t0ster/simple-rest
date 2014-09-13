from django.db import models
from django.contrib.auth.models import User


class NewsItem(models.Model):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(User)
    published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title
