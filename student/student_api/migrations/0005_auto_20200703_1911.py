# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-03 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0004_student_grade_sg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_grade',
            old_name='grade',
            new_name='marks',
        ),
    ]
