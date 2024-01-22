from django.shortcuts import render, redirect
from django.views import View

from polka.forms import AuthorForm
from polka.models import Author


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')

class AuthorView(View):
    def get(self, request):
        a = ['Adam Mickiewicz', 'Andrzej Sapkowski', 'aaaa bbbbb']
        return render(request, 'authors.html', {'authors':a})

class AddAuthorView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'add_author.html', {'formularz':form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data['first_name']
            nazwisko = form.cleaned_data['last_name']
            Autor = Author.objects.create(first_name=imie, last_name=nazwisko)
            return redirect('add_author')
        return render(request, 'add_author.html', {'formularz': form})
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
