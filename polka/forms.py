from django import forms
from django.core.exceptions import ValidationError


def check_len(value):
    if len(value)<3:
        raise ValidationError('nie ma tak krutkich imion')

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50,label="", required=True,
                                 widget=forms.TextInput(attrs={'class': 'jajko', 'placeholder': 'Imie'}),
                                 validators=[check_len])
    last_name = forms.CharField(max_length=50, validators=[check_len])

