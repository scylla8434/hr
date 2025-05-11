# HR Management System

A comprehensive HR Management System built with Django and MySQL, featuring Performance Evaluation and Benefits Administration.

## Features

- Performance Evaluation Tool
  - Performance reviews
  - Goal setting
  - Feedback management
  - Self-assessment
  - 360-degree feedback

- Benefits Administration
  - Health insurance management
  - Retirement plans
  - Wellness programs
  - Online enrollment
  - Benefits information access

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MySQL database:
- Create a database named 'hr_management'
- Update database settings in .env file

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `hr_management/` - Main project directory
- `performance/` - Performance evaluation app
- `benefits/` - Benefits administration app
- `users/` - User management app
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files

## Technologies Used

- Python 3.8+
- Django 5.0.1
- MySQL
- Bootstrap 5
- Django REST Framework
- Django AllAuth 