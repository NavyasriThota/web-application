from django.db import models


class HRProfile(models.Model):
    name = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=200)
    notes = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.company})'
