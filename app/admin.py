from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Session_Time)
admin.site.register(Student)
