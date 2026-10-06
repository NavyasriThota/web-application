# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from .forms import HRProfileForm
from .models import HRProfile


@login_required
@admin_required
def hr_list(request):
    hrs = HRProfile.objects.all()
    return render(request, 'hr_list.html', {'hrs': hrs})


@login_required
@admin_required
def hr_create(request):
    if request.method == 'POST':
        form = HRProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'HR profile created successfully.')
            return redirect('hr_list')
    else:
        form = HRProfileForm()
    return render(request, 'hr_form.html', {'form': form, 'title': 'Add HR'})


@login_required
@admin_required
def hr_detail(request, pk):
    hr = get_object_or_404(HRProfile, pk=pk)
    return render(request, 'hr_detail.html', {'hr': hr})


@login_required
@admin_required
def hr_update(request, pk):
    hr = get_object_or_404(HRProfile, pk=pk)
    if request.method == 'POST':
        form = HRProfileForm(request.POST, instance=hr)
        if form.is_valid():
            form.save()
            messages.success(request, 'HR profile updated successfully.')
            return redirect('hr_detail', pk=hr.pk)
    else:
        form = HRProfileForm(instance=hr)
    return render(request, 'hr_form.html', {'form': form, 'title': 'Update HR'})


@login_required
@admin_required
def hr_delete(request, pk):
    hr = get_object_or_404(HRProfile, pk=pk)
    hr.delete()
    messages.success(request, 'HR profile deleted successfully.')
    return redirect('hr_list')
