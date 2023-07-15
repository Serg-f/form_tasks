from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from task3.forms import TaskForm
from .models import Task
from django.forms import modelformset_factory


def create(request):
    TaskFormSet = modelformset_factory(model=Task, form=TaskForm, extra=9)
    if request.method == 'POST':
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Tasks created successfully.')
            return redirect('task3_create')
        else:
            messages.error(request, 'Error occurred while creating tasks.')
    else:
        formset = TaskFormSet()
    context = {
        'formset': formset,
        'tasks': Task.objects.all()
    }
    print('hello')
    print(*context['tasks'])
    return render(request, 'create1.html', context)
    # return render(request, 'test_formset.html', context)
