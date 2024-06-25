# admin.py
from django.contrib import admin
from .models import Stu

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

admin.site.register(Stu, StudentAdmin)
