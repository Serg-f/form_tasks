from django import forms
from django.core.exceptions import ValidationError


def len_valid(value):
    if len(value) < 10:
        raise ValidationError('Length must be more than 10 symbols')
    return value


class ContactForm(forms.Form):
    name = forms.CharField(help_text='Please, enter your fucking name, moron!')
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(), validators=[len_valid])
