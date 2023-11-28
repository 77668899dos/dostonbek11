from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
        (2, 'USTOZ'),
        (3,'STUDENT'),
    )
    user_type = models.CharField(choices=USER,max_length=50,default=3)
    profile_pic = models.ImageField(upload_to='profile_pic')

class Course(models.Model):
    name = models.CharField(max_length=50)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_Time(models.Model):
    sesstion_start = models.CharField(max_length=100)
    sesstion_end = models.CharField(max_length=100)

    def __str__(self):
        return self.sesstion_start + ' dan ' + self.sesstion_end + ' gacha'

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session_Time,on_delete=models.DO_NOTHING,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.admin.first_name + ' ' + self.admin.last_name