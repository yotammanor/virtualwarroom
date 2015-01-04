from django.db import models
from django.contrib.auth.models import User, Permission
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
    constraints = models.ManyToManyField(Permission, related_name='tasks_constrained')


class TaskEvent(models.Model):
    task = models.ForeignKey(Task, related_name='events')
    time = models.DateTimeField(auto_now=True)
    contributor = models.ForeignKey(User, related_name='contributions')


class Category(models.Model):
    name = models.CharField(max_length=256, null=False)


class FollowUp(models.Model):
    name = models.CharField(max_length=256, null=False)