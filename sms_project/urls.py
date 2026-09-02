from django.contrib import admin
from django.urls import path, include
from home import views as home_views

admin.site.site_header = "Student Management System"
admin.site.site_title = "SMS Admin"
admin.site.index_title = "Welcome to SMS Dashboard"

urlpatterns = [
    path('', home_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
]