# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.db import models


class Interview(models.Model):
    RESULT_PENDING = 'pending'
    RESULT_PASS = 'pass'
    RESULT_FAIL = 'fail'
    RESULT_CHOICES = [
        (RESULT_PENDING, 'Pending'),
        (RESULT_PASS, 'Pass'),
        (RESULT_FAIL, 'Fail'),
    ]

    student = models.ForeignKey(
        'students.StudentProfile',
        on_delete=models.CASCADE,
        related_name='interviews',
    )
    date_time = models.DateTimeField()
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    result = models.CharField(max_length=20, choices=RESULT_CHOICES, default=RESULT_PENDING)
    hr = models.ForeignKey(
        'hr_management.HRProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='interviews',
    )
    hr_name = models.CharField(max_length=150, blank=True, default='')
    hr_contact_number = models.CharField(max_length=25, blank=True, default='')
    hr_email = models.EmailField(blank=True, default='')
    job_link = models.URLField(blank=True, default='')
    rounds = models.JSONField(default=list, blank=True)
    final_result = models.CharField(max_length=20, choices=RESULT_CHOICES, default=RESULT_PENDING)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        hr = self.hr
        if hr is not None:
            self.hr_name = hr.name
            self.hr_contact_number = hr.contact_number
            self.hr_email = hr.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student} - {self.company_name} - {self.role}'
