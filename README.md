# 🎓 Student Management System

A web-based Student Management System built with Django, covering student registration, attendance tracking, results/marks management, and performance reporting.

## Features

- **Student Registration** – Add and manage student profiles (name, roll number, class, contact info)
- **Attendance Management** – Mark and track daily attendance per student
- **Results & Marks** – Record exam results by subject and exam type
- **Performance Reports** – Auto-calculated attendance % and average marks per student
- **Admin Dashboard** – Manage all data through Django's built-in admin panel

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** Django Templates, Bootstrap 5

## Setup Instructions

1. Clone the repository
   \`\`\`bash
   git clone https://github.com/YOUR_USERNAME/student-management-system.git
   cd student-management-system
   \`\`\`

2. Create and activate a virtual environment

   python -m venv venv
   venv\Scripts\activate 

3. Install dependencies

   pip install django

4. Run migrations

   python manage.py migrate


5. Create an admin user

   python manage.py createsuperuser

6. Run the server

   python manage.py runserver

7. Visit `http://127.0.0.1:8000/` in your browser


## Author

Kumar Vuyyuru