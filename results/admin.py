from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam_type', 'marks_obtained', 'max_marks')
    list_filter = ('exam_type', 'subject')
    search_fields = ('student__first_name', 'student__last_name', 'student__roll_number')