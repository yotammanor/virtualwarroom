# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='constraints',
            field=models.ManyToManyField(related_name='tasks_constrained', to='auth.Group'),
            preserve_default=True,
        ),
    ]
