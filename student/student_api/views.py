# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from student_api.models import *
from student_api.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class studentlist(APIView):

    def get(self, request):
        model = student_info.objects.all()
        serializer = student_list_serializer(model, many=True)
        return Response(serializer.data)

class studentdetails(APIView):

    def get(self,request):
        model = student_info.objects.all()
        serializer = student_serializer(instance=model,many=True)
        return Response(serializer.data)

class student_specific(APIView):

    def get(self,request,roll):
        model = student_info.objects.get(roll_no=roll)
        serializer =student_serializer(model)
        return Response(serializer.data)

class student_grade_view(APIView):
    def get(self,request):
        model = student_grade.objects.all()
        serializer = full_details_serializer(model, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializers = full_details_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)