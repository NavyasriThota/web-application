from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_STUDENT = 'student'
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_STUDENT, 'Student'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_STUDENT)
    phone = models.CharField(max_length=20, blank=True, default='')

    @property
    def is_admin_user(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_student_user(self):
        return self.role == self.ROLE_STUDENT

    def __str__(self):
        return self.get_full_name() or self.username
