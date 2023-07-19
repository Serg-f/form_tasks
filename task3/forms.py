from django import forms
from django.core.exceptions import ValidationError

from .models import Task


def valid_empty(value):
    if not len(value):
        raise ValidationError('Fill this field.')


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']
        widgets = {
            'priority': forms.Select(attrs={
                'class': 'select-item'
            }),
        }

    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) < 20:
            raise ValidationError('Description must be more than 20 symbols!')
        return data
