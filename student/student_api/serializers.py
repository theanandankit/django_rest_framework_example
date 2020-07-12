from rest_framework import serializers
from student_api.models import *

class student_list_serializer(serializers.ModelSerializer):
    roll_no=serializers.CharField(required=False)
    name=serializers.CharField(required=False)
    branch=serializers.CharField(required=False)
    class Meta:
        model = student_info
        fields="__all__"

class full_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = student_grade
        fields='__all__'

class student_serializer(serializers.ModelSerializer):
    s_g=full_details_serializer(many=True)

    class Meta:
        model = student_info
        fields=['roll_no','name','s_g']
        depth=1
