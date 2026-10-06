# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render

from accounts.decorators import admin_required, student_required
from batches.models import Batch
from hr_management.models import HRProfile
from interviews.models import Interview
from students.models import StudentProfile


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard_redirect')
    return render(request, 'landing.html')


@login_required
def dashboard_redirect(request):
    if request.user.is_admin_user:
        return redirect('admin_dashboard')
    return redirect('student_dashboard')


@login_required
@admin_required
def admin_dashboard(request):
    students = StudentProfile.objects.select_related('user', 'batch').all()
    batches = Batch.objects.annotate(student_count=Count('students')).all()
    interviews = Interview.objects.select_related('student', 'student__user', 'hr').order_by('-date_time')[:8]
    hrs = HRProfile.objects.all()

    context = {
        'students': students,
        'batches': batches,
        'interviews': interviews,
        'hrs': hrs,
        'student_count': students.count(),
        'batch_count': batches.count(),
        'interview_count': interviews.count(),
    }
    return render(request, 'dashboard_admin.html', context)


@login_required
@student_required
def student_dashboard(request):
    profile = getattr(request.user, 'student_profile', None)
    if profile is None:
        messages.warning(request, 'Complete your student profile to unlock the dashboard.')
        return redirect('student_create')

    interviews = profile.interviews.select_related('hr').order_by('-date_time')
    return render(request, 'dashboard_student.html', {'profile': profile, 'interviews': interviews})
