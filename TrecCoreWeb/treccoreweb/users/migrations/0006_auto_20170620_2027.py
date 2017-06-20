# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-20 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0007_auto_20170620_2027'),
        ('users', '0005_auto_20170620_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='current_topic',
        ),
        migrations.AddField(
            model_name='user',
            name='current_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topic.Task'),
        ),
    ]
