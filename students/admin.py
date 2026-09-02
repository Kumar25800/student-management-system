from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'first_name', 'last_name', 'student_class', 'section', 'gender')
    search_fields = ('first_name', 'last_name', 'roll_number')
    list_filter = ('student_class', 'gender')