# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
