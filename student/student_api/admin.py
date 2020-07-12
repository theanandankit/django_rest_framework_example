# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from student_api.models import student_info,student_grade

admin.site.register(student_info)
admin.site.register(student_grade)