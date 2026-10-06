from django.contrib import admin

from .models import Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'capacity', 'student_count')
    search_fields = ('name',)
