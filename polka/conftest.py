import pytest

from polka.models import Author, Genre


@pytest.fixture
def author():
    return Author.objects.create(first_name='Sławomir', last_name='Bogusławski')


@pytest.fixture
def genre():
    return Genre.objects.create(name='komedia')


@pytest.fixture
def list_genre():
    x = [Genre.objects.create(name='aaa'),
         Genre.objects.create(name='aab'),
         Genre.objects.create(name='aac'),
         Genre.objects.create(name='bbb'),
         Genre.objects.create(name='bcc'),
         Genre.objects.create(name='bca')]
    return x
