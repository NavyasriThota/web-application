# pyright: reportAttributeAccessIssue=false
# pyright: reportGeneralTypeIssues=false
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.decorators import admin_required
from .forms import BatchForm
from .models import Batch


@login_required
@admin_required
def batch_list(request):
    batches = Batch.objects.all()
    return render(request, 'batch_list.html', {'batches': batches})


@login_required
@admin_required
def batch_create(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Batch created successfully.')
            return redirect('batch_list')
    else:
        form = BatchForm()
    return render(request, 'batch_form.html', {'form': form, 'title': 'Create Batch'})


@login_required
@admin_required
def batch_detail(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    return render(request, 'batch_detail.html', {'batch': batch})


@login_required
@admin_required
def batch_update(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Batch updated successfully.')
            return redirect('batch_detail', pk=batch.pk)
    else:
        form = BatchForm(instance=batch)
    return render(request, 'batch_form.html', {'form': form, 'title': 'Update Batch'})


@login_required
@admin_required
def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    batch.delete()
    messages.success(request, 'Batch deleted successfully.')
    return redirect('batch_list')
