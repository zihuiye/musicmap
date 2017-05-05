# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mapmusic',
            fields=[
                ('musicid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('lat', models.CharField(max_length=30)),
                ('lng', models.CharField(max_length=30)),
                ('uploaderemail', models.EmailField(max_length=254)),
                ('uploadetime', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
    ]