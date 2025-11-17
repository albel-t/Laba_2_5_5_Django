from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")
    email = models.EmailField(verbose_name="Email")
    birth_date = models.DateField(verbose_name="Дата рождения")
    country = models.CharField(max_length=50, verbose_name="Страна")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступна'),
        ('borrowed', 'Выдана'),
        ('reserved', 'Зарезервирована'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    categories = models.ManyToManyField(Category, verbose_name="Категории")
    publication_date = models.DateField(verbose_name="Дата публикации")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    pages = models.IntegerField(verbose_name="Количество страниц")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available', verbose_name="Статус")
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']
    
    def __str__(self):
        return self.title