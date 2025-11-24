from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('journals/international/', views.international_journals, name='international_journals'),
    path('articles/author/<int:author_id>/', views.articles_by_author, name='articles_by_author'),
]