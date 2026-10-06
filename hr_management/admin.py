from django.contrib import admin

from .models import HRProfile


@admin.register(HRProfile)
class HRProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'contact_number')
    search_fields = ('name', 'company', 'email')
