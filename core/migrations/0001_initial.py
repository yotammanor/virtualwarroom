# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(null=True, blank=True)),
                ('link', models.URLField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ManyToManyField(related_name='tasks_assigned', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='tasks', to='core.Category')),
                ('constraints', models.ManyToManyField(related_name='tasks_constrained', to='auth.Permission')),
                ('creator', models.ForeignKey(related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
                ('follow_ups', models.ManyToManyField(related_name='tasks', to='core.FollowUp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('contributor', models.ForeignKey(related_name='contributions', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(related_name='events', to='core.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
