# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('youtube_id', models.CharField(max_length=100, unique=True)),
                ('published_date', models.DateTimeField()),
            ],
        ),
    ]