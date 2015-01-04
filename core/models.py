from django.db import models
from django.contrib.auth.models import User, Permission, Group
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=256, null=False)
    description = models.TextField(null=True, blank=True)
    link = models.URLField()
    categories = models.ManyToManyField('Category', related_name='tasks')
    follow_ups = models.ManyToManyField('FollowUp', related_name='tasks')
    time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='tasks_created', null=False)
    assigned_to = models.ManyToManyField(User, related_name='tasks_assigned')
    constraints = models.ManyToManyField(Group, related_name='tasks_constrained')
    status = models.CharField(max_length=16, null=False, choices=(('Open', 'Open'), ('Completed', 'Completed'),),
                              default='Open')

    def __unicode__(self):
        return self.title


class TaskEvent(models.Model):
    task = models.ForeignKey(Task, related_name='events')
    time = models.DateTimeField(auto_now=True)
    contributor = models.ForeignKey(User, related_name='contributions')
    action = models.CharField(max_length=256, null=False, default='')

    def __unicode__(self):
        return '%s: %s' % (str(self.date_of_creation.date()), self.action)


class Category(models.Model):
    name = models.CharField(max_length=256, null=False)
    follow_ups = models.ManyToManyField('FollowUp', related_name='categories')

    def __unicode__(self):
        return self.name


class FollowUp(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return self.name