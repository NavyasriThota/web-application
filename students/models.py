# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.conf import settings
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
    )
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=150)
    skills = models.TextField()
    experience = models.CharField(max_length=200, blank=True, default='')
    joining_date = models.DateField()
    batch = models.ForeignKey(
        'batches.Batch',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.get_full_name() or self.user.username)
