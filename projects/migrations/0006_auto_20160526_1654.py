# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 20:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160526_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='date_involved',
            new_name='date_first_involved',
        ),
        migrations.AddField(
            model_name='membership',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 26, 20, 54, 2, 621345, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
