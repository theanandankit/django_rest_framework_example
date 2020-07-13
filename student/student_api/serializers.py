from rest_framework import serializers
from student_api.models import *
from django.contrib.auth.models import User

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

class register_user(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']
        write_only_fields = ('password',)

    def create(self, validated_data):
        users = User.objects.create(
             username=validated_data['username'],
        )
        users.set_password(validated_data['password'])
        users.save()
        return users
