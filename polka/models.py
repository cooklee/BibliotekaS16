import uuid
from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='')


class Genre(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse('detail_book', args=(self.id,))

    def __str__(self):
        return self.title
