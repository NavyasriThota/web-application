from django import forms

from .models import HRProfile


class HRProfileForm(forms.ModelForm):
    class Meta:
        model = HRProfile
        fields = ['name', 'contact_number', 'email', 'company', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
