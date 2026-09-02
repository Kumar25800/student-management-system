from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('student/<int:student_id>/', views.student_report_detail, name='student_report_detail'),
]