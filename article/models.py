from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author)
    
    def __str__(self):
        return self.name

class Journal(models.Model):
    LEVEL_CHOICES = [
        ('national', 'Национальный'),
        ('international', 'Международный'),
        ('regional', 'Региональный'),
    ]
    
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES, null=True, blank=True)
    articles = models.ForeignKey(Article, on_delete=models.PROTECT)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name