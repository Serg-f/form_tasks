from django import forms
from django.core.exceptions import ValidationError

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) < 20:
            raise ValidationError('Description must be more than 20 symbols!')
        return data
