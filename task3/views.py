from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from task3.forms import TaskForm
from .models import Task
from django.forms import modelformset_factory

TaskFormSet = modelformset_factory(model=Task, fields=('title', 'description'), extra=4)


def create(request):
    if request.method == 'POST':
        pass
    else:
        formset = TaskFormSet()
    context = {
        'formset': formset,
    }
    return render(request, 'create.html', context)
