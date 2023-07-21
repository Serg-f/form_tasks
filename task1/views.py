from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'task1/index.html')


def task1(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name, email, message = form.cleaned_data.values()
            messages.success(request, 'The form data is valid.')
            messages.success(request, f'User "{name}" with email "{email}" sent next message:')
            messages.success(request,  f'"{message}"')
    else:
        form = ContactForm()
    return render(request, 'task1/task1_form.html', {'form': form})
