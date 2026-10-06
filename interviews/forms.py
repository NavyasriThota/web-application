from django import forms

from .models import Interview


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [
            'student', 'date_time', 'company_name', 'role', 'result', 'hr',
            'job_link', 'rounds', 'final_result', 'notes'
        ]
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'rounds': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Example: ["Screening", "Technical", "Manager Round"]'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
