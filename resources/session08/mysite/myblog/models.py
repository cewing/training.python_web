from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def author_name(self):
        raw_name = "%s %s" % (self.author.first_name,
                              self.author.last_name)
        name = raw_name.strip()
        if not name:
            name = self.author.username
        return name


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, 
        blank=True,
        null=True,
        related_name='categories'
    )

    def __unicode__(self):
        return self.name

