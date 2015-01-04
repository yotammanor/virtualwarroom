# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150104_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='follow_ups',
            field=models.ManyToManyField(related_name='categories', to='core.FollowUp'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'Open', max_length=16, choices=[(b'Open', b'Open'), (b'Completed', b'Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskevent',
            name='action',
            field=models.CharField(default=b'', max_length=256),
            preserve_default=True,
        ),
    ]
