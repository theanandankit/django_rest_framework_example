# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-02 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='roll_no',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
