from django.shortcuts import render, get_object_or_404
from students.models import Student
from attendance.models import Attendance
from results.models import Result
from django.db.models import Avg, Count, Q

def report_list(request):
    students = Student.objects.all()
    report_data = []

    for student in students:
        total_days = Attendance.objects.filter(student=student).count()
        present_days = Attendance.objects.filter(student=student, status='P').count()
        attendance_pct = round((present_days / total_days) * 100, 2) if total_days > 0 else 0

        avg_marks = Result.objects.filter(student=student).aggregate(avg=Avg('marks_obtained'))['avg']
        avg_marks = round(avg_marks, 2) if avg_marks else 0

        report_data.append({
            'student': student,
            'attendance_pct': attendance_pct,
            'avg_marks': avg_marks,
        })

    return render(request, 'reports/report_list.html', {'report_data': report_data})


def student_report_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendance_records = Attendance.objects.filter(student=student).order_by('-date')
    results = Result.objects.filter(student=student)

    total_days = attendance_records.count()
    present_days = attendance_records.filter(status='P').count()
    attendance_pct = round((present_days / total_days) * 100, 2) if total_days > 0 else 0

    avg_marks = results.aggregate(avg=Avg('marks_obtained'))['avg']
    avg_marks = round(avg_marks, 2) if avg_marks else 0

    context = {
        'student': student,
        'attendance_records': attendance_records,
        'results': results,
        'attendance_pct': attendance_pct,
        'avg_marks': avg_marks,
    }
    return render(request, 'reports/student_detail.html', context)