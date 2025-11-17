from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book, Category

def home(request):
    """Главная страница со всей информацией"""
    authors = Author.objects.all()
    books = Book.objects.all()
    categories = Category.objects.all()
    
    context = {
        'authors': authors,
        'books': books,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def available_books(request):
    """Страница с доступными книгами"""
    available_books = Book.objects.filter(status='available')
    context = {
        'books': available_books,
        'filter_name': 'Доступные книги'
    }
    return render(request, 'books_list.html', context)

def books_by_author(request, author_id):
    """Книги определенного автора"""
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    context = {
        'books': books,
        'filter_name': f'Книги автора: {author.name}'
    }
    return render(request, 'books_list.html', context)

class BookListView(ListView):
    """Класс-представление для списка книг"""
    model = Book
    template_name = 'books_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_name'] = 'Все книги'
        return context