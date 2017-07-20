# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0011_auto_20170714_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographic',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='enjoyment',
            field=models.CharField(blank=True, choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='expertise',
            field=models.CharField(blank=True, choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('MALE', 'Male'), ('FEMALE', 'Female')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='help',
            field=models.CharField(blank=True, choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='language',
            field=models.CharField(blank=True, choices=[('', ''), ('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCE', 'Advance'), ('FLUENT', 'Fluent'), ('PROFICIENT', 'Proficient'), ('NATIVE', 'Native')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='search_engine_usage',
            field=models.CharField(blank=True, choices=[('', ''), ('SEVERAL', 'Several times a day'), ('ONCE', 'At least once a day'), ('WEEK', 'At least once a week'), ('MONTH', 'At least once a month'), ('RARELY', 'Rarely (Less than one search a month on average)')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='student_degree',
            field=models.CharField(blank=True, choices=[('', ''), ('UNDERGRAD', 'An undergraduate student'), ('GRAD', 'A graduate student'), ('OTHER', 'Other. Please specify')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='student_major',
            field=models.CharField(blank=True, choices=[('', ''), ('ART', 'An art student'), ('STEM', 'A science, technology, engineering, or math student.'), ('OTHER', 'Other. Please specify')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='training',
            field=models.CharField(blank=True, choices=[('', ''), ('YES', 'Yes'), ('NO', 'No')], max_length=56, null=True),
        ),
        migrations.AlterField(
            model_name='demographic',
            name='trouble',
            field=models.CharField(blank=True, choices=[('', ''), ('STRONG_DISAGREE', 'Strongly Disagree'), ('DISAGREE', 'Disagree'), ('NEUTRAL', 'Neutral'), ('AGREE', 'Agree'), ('STRONGLY_AGREE', 'Strongly Agree')], max_length=56, null=True),
        ),
    ]
