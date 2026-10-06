from django.contrib import admin

from .models import Interview


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'company_name', 'role', 'date_time', 'result', 'final_result')
    list_filter = ('result', 'final_result')
    search_fields = ('company_name', 'role', 'student__user__username')
