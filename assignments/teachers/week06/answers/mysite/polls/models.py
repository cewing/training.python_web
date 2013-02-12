from django.db import models
from django.utils import timezone


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def published_today(self):
        now = timezone.now()
        time_delta = now - self.pub_date
        return time_delta.days == 0
    published_today.boolean = True
    published_today.short_description = "Published Today?"

    def total_votes(self):
        total = 0
        for choice in self.choice_set.all():
            total += choice.votes
        return total


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice
