# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from students.models import StudentProfile

User = get_user_model()


class RBACAndLogoutTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username='trainer',
            email='trainer@example.com',
            password='admin123',
            role=User.ROLE_ADMIN,
            first_name='Trainer',
            last_name='Admin',
        )
        self.student = User.objects.create_user(
            username='student1',
            email='student1@example.com',
            password='student123',
            role=User.ROLE_STUDENT,
            first_name='Student',
            last_name='One',
        )
        StudentProfile.objects.create(
            user=self.student,
            age=22,
            education='B.Sc. Computer Science',
            skills='Python, Django, SQL',
            experience='1 year',
            joining_date='2025-01-06',
        )

    def test_logout_requires_post(self):
        self.client.force_login(self.admin)

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 405)
        self.assertIn('_auth_user_id', self.client.session)

    def test_student_cannot_access_admin_dashboard(self):
        self.client.force_login(self.student)

        response = self.client.get(reverse('admin_dashboard'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('student_dashboard'))

    def test_student_without_profile_is_redirected_to_profile_setup(self):
        profile_less_student = User.objects.create_user(
            username='student2',
            email='student2@example.com',
            password='student123',
            role=User.ROLE_STUDENT,
        )
        self.client.force_login(profile_less_student)

        response = self.client.get(reverse('student_dashboard'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('student_create'))
