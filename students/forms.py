from django import forms

from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['user', 'age', 'education', 'skills', 'experience', 'joining_date', 'batch']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.TextInput(attrs={'placeholder': 'e.g. 2 years in software development'}),
        }
