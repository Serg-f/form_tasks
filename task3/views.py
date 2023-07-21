from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from task3.forms import TaskForm
from .models import Priority, Task
from django.forms import modelformset_factory

TaskFormSet = modelformset_factory(model=Task, form=TaskForm)
TaskFormSetExtra0 = modelformset_factory(model=Task, form=TaskForm, extra=0, can_delete=True)


def create(request):
    if request.method == 'POST':
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Tasks have been created successfully.')
            return redirect('create')
    else:
        formset = TaskFormSet(queryset=Task.objects.none())
    context = {
        'formset': formset,
        'priorities': Priority.objects.all()
    }
    return render(request, 'task3/create.html', context)


def edit(request, priority_id):
    priority = get_object_or_404(Priority, id=priority_id)
    tasks_set = Task.objects.filter(priority_id=priority_id)
    if request.method == 'POST':

        formset = TaskFormSetExtra0(data=request.POST, prefix='tasks')

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            formset.save()
            messages.success(request, f'"{priority.name}" priority tasks have been edited successfully.')
            return redirect('create')
    else:
        formset = TaskFormSetExtra0(queryset=tasks_set, prefix='tasks')

    context = {
        'formset': formset,
        'priorities': Priority.objects.all(),
        'priority': priority,
    }
    return render(request, 'task3/edit.html', context)
