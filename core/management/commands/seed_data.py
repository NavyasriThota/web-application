# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from datetime import date

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from batches.models import Batch
from hr_management.models import HRProfile
from interviews.models import Interview
from students.models import StudentProfile


class Command(BaseCommand):
    help = 'Seed demo data for the institute management system.'

    def handle(self, *args, **options):
        User = get_user_model()

        admin_user, created = User.objects.get_or_create(
            username='trainer',
            defaults={
                'email': 'trainer@institute.com',
                'first_name': 'Maya',
                'last_name': 'Sharma',
                'role': User.ROLE_ADMIN,
                'phone': '+91-9876543210',
                'is_staff': True,
                'is_superuser': True,
            },
        )
        if created or not admin_user.has_usable_password():
            admin_user.set_password('admin123')
            admin_user.save()

        batch_a, _ = Batch.objects.get_or_create(
            name='Batch A - 2026',
            defaults={
                'start_date': date(2026, 1, 10),
                'end_date': date(2026, 6, 30),
                'capacity': 15,
                'description': 'Full-stack software training batch',
            },
        )
        Batch.objects.get_or_create(
            name='Batch B - 2026',
            defaults={
                'start_date': date(2026, 2, 12),
                'end_date': date(2026, 7, 20),
                'capacity': 15,
                'description': 'Data science and analytics cohort',
            },
        )

        hr_1, _ = HRProfile.objects.get_or_create(
            email='sarah@technova.com',
            defaults={
                'name': 'Sarah Johnson',
                'contact_number': '+1-415-555-0147',
                'company': 'TechNova',
                'notes': 'Builds cloud platform products',
            },
        )
        hr_2, _ = HRProfile.objects.get_or_create(
            email='arjun@pixelgrid.io',
            defaults={
                'name': 'Arjun Mehta',
                'contact_number': '+91-9988776655',
                'company': 'PixelGrid',
                'notes': 'Hiring product engineering talent',
            },
        )

        student_user, created_student = User.objects.get_or_create(
            username='student1',
            defaults={
                'email': 'student1@example.com',
                'first_name': 'Aisha',
                'last_name': 'Patel',
                'role': User.ROLE_STUDENT,
                'phone': '+91-9123456789',
            },
        )
        if created_student or not student_user.has_usable_password():
            student_user.set_password('student123')
            student_user.save()
        student_profile, _ = StudentProfile.objects.get_or_create(
            user=student_user,
            defaults={
                'age': 23,
                'education': 'B.E. Computer Science',
                'skills': 'Python, Django, SQL, JavaScript, REST APIs',
                'experience': '2 years internship experience',
                'joining_date': date(2026, 1, 15),
                'batch': batch_a,
            },
        )

        Interview.objects.get_or_create(
            student=student_profile,
            date_time='2026-10-08T14:30:00Z',
            defaults={
                'company_name': 'TechNova',
                'role': 'Python Developer',
                'result': Interview.RESULT_PENDING,
                'hr': hr_1,
                'job_link': 'https://example.com/jobs/technova-python',
                'rounds': ['Screening', 'Technical Round', 'Hiring Manager'],
                'final_result': Interview.RESULT_PENDING,
                'notes': 'Strong backend fundamentals',
            },
        )

        Interview.objects.get_or_create(
            student=student_profile,
            date_time='2026-10-15T11:00:00Z',
            defaults={
                'company_name': 'PixelGrid',
                'role': 'Junior Full Stack Engineer',
                'result': Interview.RESULT_PASS,
                'hr': hr_2,
                'job_link': 'https://example.com/jobs/pixelgrid-fullstack',
                'rounds': ['Coding', 'System Design', 'Final Discussion'],
                'final_result': Interview.RESULT_PASS,
                'notes': 'Offer awaited',
            },
        )

        self.stdout.write(self.style.SUCCESS('Demo users, students, batches, HR and interviews created successfully.'))
