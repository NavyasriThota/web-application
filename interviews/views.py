# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from .forms import InterviewForm
from .models import Interview


@login_required
def interview_list(request):
    if request.user.is_admin_user:
        interviews = Interview.objects.select_related('student', 'student__user', 'hr').all().order_by('-date_time')
    else:
        interviews = Interview.objects.filter(student__user=request.user).select_related('student', 'student__user', 'hr').order_by('-date_time')
    return render(request, 'interview_list.html', {'interviews': interviews})


@login_required
@admin_required
def interview_create(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Interview record created successfully.')
            return redirect('interview_list')
    else:
        form = InterviewForm()
    return render(request, 'interview_form.html', {'form': form, 'title': 'Create Interview'})


@login_required
def interview_detail(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    if not request.user.is_admin_user and request.user != interview.student.user:
        return redirect('student_dashboard')
    return render(request, 'interview_detail.html', {'interview': interview})


@login_required
@admin_required
def interview_update(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            messages.success(request, 'Interview updated successfully.')
            return redirect('interview_detail', pk=interview.pk)
    else:
        form = InterviewForm(instance=interview)
    return render(request, 'interview_form.html', {'form': form, 'title': 'Update Interview'})


@login_required
@admin_required
def interview_delete(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    interview.delete()
    messages.success(request, 'Interview deleted successfully.')
    return redirect('interview_list')
