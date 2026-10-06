from django.contrib import admin

from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'education', 'batch', 'joining_date')
    list_filter = ('batch',)
    search_fields = ('user__username', 'user__email', 'education')
