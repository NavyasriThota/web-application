# InstituteHub Management System

A Django-based institute management platform built for admins and students. It supports:

- Admin dashboard with full CRUD for students, batches, HR records, and interviews
- Student dashboard with profile and self-service updates
- JWT-based login endpoints for APIs
- Local PostgreSQL-ready configuration with SQLite fallback for quick startup
- Professional dashboard UI using Django templates and a custom CSS theme

## Tech Stack

- Django 6.x
- PostgreSQL (recommended for local dev)
- Django REST Framework
- JWT via djangorestframework-simplejwt
- Bootstrap-like custom CSS UI

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and update PostgreSQL values if using a local database.
4. Create the database in PostgreSQL if needed:
   ```sql
   CREATE DATABASE institute_db;
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Seed demo data:
   ```bash
   python manage.py seed_data
   ```
7. Start the app:
   ```bash
   python manage.py runserver
   ```

## Default Demo Accounts

- Admin: `trainer` / `admin123`
- Student: `student1` / default password is not set for student account unless created through Django admin. Use Django admin to set a password or use the admin user to create a student account.

## Route Overview

- `/` landing page
- `/login/` login
- `/dashboard/admin/` admin dashboard
- `/dashboard/student/` student dashboard
- `/students/` student directory
- `/batches/` batch management
- `/hr/` HR directory
- `/interviews/` interview management
- `/api/auth/token/` JWT access token endpoint
- `/api/auth/token/refresh/` JWT refresh endpoint

## Notes

The application is configured to use PostgreSQL automatically when `POSTGRES_DB` or `DB_ENGINE=postgresql` is present in the environment. Without those values, Django falls back to SQLite for local development convenience.
