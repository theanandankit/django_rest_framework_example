# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save

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
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)    