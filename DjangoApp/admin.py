from django.contrib import admin
from .models import Author, Category, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'is_active']  # Показываем только 3 из 5 полей
    list_filter = ['country']  # Фильтр по стране
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  # Показываем только 2 из 3 полей
    list_filter = ['created_at']  # Фильтр по дате создания

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date', 'status']  # Показываем 4 из 8 полей
    list_filter = ['status', 'publication_date']  # Фильтр по статусу и дате публикации
    filter_horizontal = ['categories']  # Для удобного выбора категорий
    search_fields = ['title', 'author__name']