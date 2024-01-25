import pytest
from django.test import Client
from django.urls import reverse

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
