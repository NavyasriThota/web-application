# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from .forms import StudentProfileForm
from .models import StudentProfile


@login_required
@admin_required
def student_list(request):
    students = StudentProfile.objects.select_related('user', 'batch').all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def student_create(request):
    if request.user.is_admin_user:
        pass
    elif getattr(request.user, 'student_profile', None):
        return redirect('student_dashboard')

    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if not request.user.is_admin_user:
            form.fields['user'].disabled = True
            form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Student profile created successfully.')
            return redirect('student_dashboard' if not request.user.is_admin_user else 'student_list')
    else:
        form = StudentProfileForm()
        if not request.user.is_admin_user:
            form.fields['user'].disabled = True
            form.initial['user'] = request.user.pk
    return render(request, 'student_form.html', {'form': form, 'title': 'Create Student'})


@login_required
def student_detail(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    if not request.user.is_admin_user and request.user != profile.user:
        return redirect('student_dashboard')
    return render(request, 'student_detail.html', {'profile': profile})


@login_required
def student_update(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    if not request.user.is_admin_user and request.user != profile.user:
        return redirect('student_dashboard')

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if not request.user.is_admin_user:
            form.fields['user'].disabled = True
            form.instance.user = profile.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Student details updated successfully.')
            return redirect('student_detail', pk=profile.pk)
    else:
        form = StudentProfileForm(instance=profile)
        if not request.user.is_admin_user:
            form.fields['user'].disabled = True

    return render(request, 'student_form.html', {'form': form, 'title': 'Update Student', 'profile': profile})


@login_required
@admin_required
def student_delete(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    profile.delete()
    messages.success(request, 'Student profile deleted successfully.')
    return redirect('student_list')
