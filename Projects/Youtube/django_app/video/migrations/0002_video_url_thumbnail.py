# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url_thumbnail',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
