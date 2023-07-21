from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from task2.forms import TaskForm
from .models import Task


def create(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'New task "{form.cleaned_data.get("title")}" has been successfully created!')
            return redirect('create')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'tasks': Task.objects.all().order_by('-id')
    }
    return render(request, 'task2/create.html', context)


def edit(request, task_id):
    task_inst = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task_inst)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task_inst.title}" has been successfully edited')
            return redirect('create')
    else:
        form = TaskForm(instance=task_inst)
    context = {
        'form': form,
        'tasks': Task.objects.all().order_by('-id'),
        'task_inst': task_inst,
    }
    return render(request, 'task2/edit.html', context)
