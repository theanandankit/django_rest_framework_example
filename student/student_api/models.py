# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class student_info(models.Model):
    roll_no=models.CharField(max_length=15,unique=True,primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class student_grade(models.Model):
    sg=models.ForeignKey(student_info,on_delete=models.CASCADE,default='ankit',related_name='s_g')
    marks=models.CharField(max_length=5)

    def __str__(self):
        return self.marks
    