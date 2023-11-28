from rest_framework import serializers
from app.models import CustomUser,Student

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','user_type','username','first_name')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('admin','address','gender','course_id','session_id','created_at','updated_at')

