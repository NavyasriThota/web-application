# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.core.exceptions import ValidationError
from django.db import models


class Batch(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.PositiveIntegerField(default=15)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['start_date']

    def clean(self):
        if self.students.count() > self.capacity:
            raise ValidationError('This batch is full and exceeds the requested capacity.')

    @property
    def student_count(self):
        return self.students.count()

    def __str__(self):
        return str(self.name)
