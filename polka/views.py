from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView

from polka.forms import AuthorForm, PublisherAddForm, GenreAddForm, AddBookForm, GenreSearchForm, BookSearchForm
from polka.models import Author, Book, Genre


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


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


class AddGenreView(LoginRequiredMixin, View):

    def get(self, request):
        form = GenreAddForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):
        form = GenreAddForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return redirect('add_genre')
        return render(request, 'add_form.html', {'form': form})


class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'add_form.html'
    success_url = reverse_lazy('add_book')


class ListBookView(ListView):
    model = Book
    template_name = 'list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = BookSearchForm()
        context['xxx'] = 'ala ma pieska'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = BookSearchForm(self.request.GET)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            queryset = queryset.filter(title__icontains=title)
            if author is not None:
                queryset = queryset.filter(authors=author)
        return queryset


class DetailGenreView(View):
    def get(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        return render(request, 'detail_genre_view.html', {'genre': genre})


class DetailBookView(View):

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'detail_book_view.html', {'book': book})


class ListGenreView(View):
    def get(self, request):
        genres = Genre.objects.all()
        form = GenreSearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            genres = genres.filter(name__icontains=name)

        return render(request, 'list_view.html', {'object_list': genres, 'form': form})


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
