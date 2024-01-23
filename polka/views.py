from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from polka.forms import AuthorForm, PublisherAddForm, GenreAddForm, AddBookForm
from polka.models import Author, Book


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')


class AuthorView(View):
    def get(self, request):
        a = ['Adam Mickiewicz', 'Andrzej Sapkowski', 'aaaa bbbbb']
        return render(request, 'authors.html', {'authors': a})


class AddAuthorView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data['first_name']
            nazwisko = form.cleaned_data['last_name']
            autor = Author.objects.create(first_name=imie, last_name=nazwisko)
            return redirect('add_author')
        return render(request, 'add_form.html', {'form': form})


class AddPublisherView(View):

    def get(self, request):
        form = PublisherAddForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):
        form = PublisherAddForm(request.POST)
        if form.is_valid():
            publisher = form.save()
            return redirect('add_form')
        return render(request, 'add_form.html', {'form': form})


class AddGenreView(View):

    def get(self, request):
        form = GenreAddForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):
        form = GenreAddForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return redirect('add_genre')
        return render(request, 'add_form.html', {'form': form})


class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'add_form.html'
    success_url = reverse_lazy('add_book')


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {'zmienna1': 'ala ma kota',
                                              'zmienna2': 'wlaz kotek na płotek'})


class Index2View(View):
    def get(self, request):
        lst = [
            'niebieski', 'czerwony', 'zielony', 'sinokoperkowyróż'
        ]
        return render(request, 'index.html', {'zmienna1': 'Ola Boga moja noga',
                                              'zmienna2': 'Srali muszki bedzie wiosna', 'lista': lst})
