from django.shortcuts import render
from .models import Author, Article, Journal

def home(request):
    """Главная страница со всеми данными"""
    authors = Author.objects.all()
    articles = Article.objects.all()
    journals = Journal.objects.all()
    
    context = {
        'authors': authors,
        'articles': articles,
        'journals': journals,
    }
    return render(request, 'article/home.html', context)

def international_journals(request):
    """Журналы международного уровня"""
    journals = Journal.objects.filter(level='international')
    context = {
        'journals': journals,
        'filter_name': 'Международные журналы'
    }
    return render(request, 'article/journals_list.html', context)

def articles_by_author(request, author_id):
    """Статьи определенного автора"""
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(authors=author)
    context = {
        'articles': articles,
        'filter_name': f'Статьи автора: {author.first_name} {author.last_name}'
    }
    return render(request, 'article/articles_list.html', context)