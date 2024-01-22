from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50,label="", widget=forms.PasswordInput(attrs={'class': 'jajko', 'placeholder': 'Imie'}))
    last_name = forms.CharField(max_length=50)

