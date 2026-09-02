from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=20)  # e.g. "10th", "BSc-1"
    section = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_admitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"