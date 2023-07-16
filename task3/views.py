from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from task3.forms import TaskForm
from .models import Task
from django.forms import modelformset_factory

TaskFormSet = modelformset_factory(model=Task, form=TaskForm)


def create(request):
    if request.method == 'POST':
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Tasks created successfully.')
            return redirect('task3_create')
    else:
        formset = TaskFormSet(queryset=Task.objects.none())
    context = {
        'formset': formset,
        'tasks': Task.objects.all()
    }
    return render(request, 'create1.html', context)
