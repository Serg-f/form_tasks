from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def task1(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, 'task1_form.html', {'form': form})
