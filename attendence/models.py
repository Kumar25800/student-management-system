from django.db import models
from students.models import Student

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    class Meta:
        unique_together = ('student', 'date')  # one attendance record per student per day

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"