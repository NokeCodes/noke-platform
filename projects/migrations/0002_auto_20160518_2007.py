# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_requested',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
