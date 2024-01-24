from django.contrib import admin

from polka.models import Book, Genre, Author, Comment

# Register your models he
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Comment)