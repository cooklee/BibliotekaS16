"""
URL configuration for BibliotekaS16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from polka import views


urlpatterns = [
    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('addAuthor/', views.AddAuthorView.as_view(), name='add_author'),
    path('addPublisher/', views.AddPublisherView.as_view(), name='add_publisher'),
    path('addGenre/', views.AddGenreView.as_view(), name='add_genre'),
    path('addBook/', views.AddBookView.as_view(), name='add_book'),
    path('listBook/', views.ListBookView.as_view(), name='list_book'),
    path('detailBook/<int:pk>/', views.DetailBookView.as_view(), name='detail_book'),
    path('detailGenre/<int:pk>/', views.DetailGenreView.as_view(), name='detail_genre'),
    path('listGenre/', views.ListGenreView.as_view(), name='list_genre'),
    path('v/', views.Index2View.as_view(), name='index2'),
    path('addComent/<int:book_pk>/', views.AddCommentView.as_view(), name='add_comment')
]
