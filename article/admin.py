from django.contrib import admin
from .models import Journal, Article, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country']  # Показываем 3 из 5 полей
    list_filter = ['country']  # Фильтр по стране

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']  # Показываем 2 из 5 полей
    list_filter = ['created_at']  # Фильтр по дате создания

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'publisher']  # Показываем 3 из 6 полей
    list_filter = ['level']  # Фильтр по уровню