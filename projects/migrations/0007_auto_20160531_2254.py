# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 02:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160526_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 1, 2, 54, 18, 395696, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
