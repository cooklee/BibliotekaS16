import pytest
from django.test import Client
from django.urls import reverse

from polka.forms import AuthorForm
from polka.models import Book, Author


@pytest.mark.django_db
def test_list_genre(list_genre):
    client = Client()   # stworzenie przeglądarki
    url = reverse('list_genre') # pobranie adresu na który chcem wejsć
    response = client.get(url) # wchodzimy na ten adres i dop zapisujemy w zmienne response
    assert response.status_code == 200 #sprawdzamy status code odpowiedzi
    assert response.context['object_list'].count() == len(list_genre)
    for genre in list_genre:
        assert genre in response.context['object_list']

@pytest.mark.django_db
def test_search_genre(list_genre):
    client = Client()   # stworzenie przeglądarki
    url = reverse('list_genre') # pobranie adresu na który chcem wejsć
    url = f'{url}?name=ab'
    response = client.get(url) # wchodzimy na ten adres i dop zapisujemy w zmienne response
    assert response.status_code == 200 #sprawdzamy status code odpowiedzi
    assert response.context['object_list'].count() == 1
    assert response.context['object_list'][0] == list_genre[1]


@pytest.mark.django_db
def test_addAuthor_get():
    client = Client()
    url = reverse('add_author')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AuthorForm)


@pytest.mark.django_db
def test_addAuthor_post():
    client = Client()
    url = reverse('add_author')
    data = {
        'first_name':'sławek',
        'last_name':'bogusławski'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Author.objects.get(first_name=data['first_name'],
                              last_name=data['last_name'])
@pytest.mark.django_db
def test_addbook_not_login():
    client = Client()
    url = reverse('add_book')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login_view'))

@pytest.mark.django_db
def test_add_book_no_permission(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_book')
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_addBook_post(author, list_genre, user_with_book_permission):
    client = Client()
    client.force_login(user_with_book_permission)
    url = reverse('add_book')
    data = {
        'title':'noce i dnie',
        'authors':author.id,
        'genres':[g.id for g in list_genre]
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('add_book')
    assert Book.objects.get(title=data['title'])


