from django import forms
from django.core.exceptions import ValidationError

from polka.models import Publisher, Genre, Book, Author, Comment


def check_len(value):
    if len(value)<3:
        raise ValidationError('nie ma tak krutkich imion')

class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50,label="", required=True,
                                 widget=forms.TextInput(attrs={'class': 'jajko', 'placeholder': 'Imie'}),
                                 validators=[check_len])
    last_name = forms.CharField(max_length=50, validators=[check_len])


class PublisherAddForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class GenreAddForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'genres': forms.CheckboxSelectMultiple()
        }

class GenreSearchForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']