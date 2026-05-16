# Learning Management System (LMS)

A Django-based Learning Management System (LMS) developed using Python.  
This project helps manage courses, students, and instructors in an online learning platform.

---

## 🚀 Features

- User authentication (login/register/logout)
- Student and instructor modules
- Course creation and management
- Media/image handling using Pillow
- Database integration using SQLite
- Dynamic web interface using Django

---

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML, CSS, JavaScript
- Pillow

---

## 📦 Requirements

-Django
-Pillow

# Learning Management System (LMS) - COMPLETE SETUP GUIDE
# 📌 STEP 1: Install Requirements

Make sure Python, pip, and Git are installed.

Check:
```bash
python --version
pip --version
git --version


# 📌 STEP 2:Create Virtual Environment (venv)
python -m venv venv


# 📌 STEP 3: Actiavte Virtual Environment
venv/Scripts/activate

# 📌 STEP 4: Install Dependencies
pip install django
pip install pillow

# 📌 STEP 5: Database Setup (Migrations)
python manage.py makemigrations
python manage.py migrate

# 📌 STEP 6: Create Admin User (Optional)
python manage.py createsuperuser

# 📌 STEP 7: Run Server
python manage.py runserver

open in browser
http://127.0.0.1:8000/
