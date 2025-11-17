from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/available/', views.available_books, name='available_books'),
    path('books/author/<int:author_id>/', views.books_by_author, name='books_by_author'),
]