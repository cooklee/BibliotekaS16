from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from polka.forms import AuthorForm, PublisherAddForm, GenreAddForm, AddBookForm, GenreSearchForm, BookSearchForm, \
    AddCommentForm
from polka.models import Author, Book, Genre, Comment, BorrowedBook


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


class AddBookView(PermissionRequiredMixin, CreateView):
    permission_required = ['polka.add_book']
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

class BorrowedBookListView(View):

    def get_queryset(self):
        return [borrowed.book for borrowed in
                 BorrowedBook.objects.filter(user=self.request.user, returned_date__isnull=True)]
    def get(self, request):
        books = self.get_queryset()

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


class AddCommentView(LoginRequiredMixin, View):

    def get(self, request, book_pk):
        form = AddCommentForm()
        return render(request, 'add_form.html', {'form':form})
    def post(self, request, book_pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = Book.objects.get(pk=book_pk)
            comment.author = self.request.user
            comment.save()
            return redirect('detail_book', book_pk)
        return render(request, 'add_form.html', {'form': form})


class EditCommentView( UserPassesTestMixin, UpdateView):
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    model = Comment
    fields = ['text']
    template_name = 'add_form.html'
    def get_success_url(self):
        return reverse('detail_book', args=(self.object.book.id,))
