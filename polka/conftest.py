import pytest
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from polka.models import Author, Genre, Book


@pytest.fixture
def author():
    return Author.objects.create(first_name='Sławomir', last_name='Bogusławski')


@pytest.fixture
def genre():
    return Genre.objects.create(name='komedia')

@pytest.fixture
def user():
    return User.objects.create(username='test')


@pytest.fixture
def user_with_book_permission(user):
    content_type = ContentType.objects.get_for_model(Book)
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    return user

@pytest.fixture
def list_genre():
    x = [Genre.objects.create(name='aaa'),
         Genre.objects.create(name='aab'),
         Genre.objects.create(name='aac'),
         Genre.objects.create(name='bbb'),
         Genre.objects.create(name='bcc'),
         Genre.objects.create(name='bca')]
    return x
