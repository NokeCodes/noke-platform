# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 02:37
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160518_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from=b'title', unique=True),
        ),
    ]