from django.db import models
from students.models import Student

class Result(models.Model):
    EXAM_TYPE_CHOICES = [
        ('MID', 'Mid Term'),
        ('FIN', 'Final Term'),
        ('UNIT', 'Unit Test'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject = models.CharField(max_length=50)
    exam_type = models.CharField(max_length=5, choices=EXAM_TYPE_CHOICES)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    exam_date = models.DateField()

    class Meta:
        unique_together = ('student', 'subject', 'exam_type')

    @property
    def percentage(self):
        return round((self.marks_obtained / self.max_marks) * 100, 2)

    def __str__(self):
        return f"{self.student} - {self.subject} ({self.exam_type}): {self.marks_obtained}/{self.max_marks}"