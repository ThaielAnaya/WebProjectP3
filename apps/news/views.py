from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articulo

class ArticleListView(ListView):
    model = Articulo
    template_name = 'news/article_list.html'
    context_object_name = 'articles'
    ordering = ['-published']
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Articulo
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

