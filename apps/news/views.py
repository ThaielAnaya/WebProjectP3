from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articulo

class ArticleListView(ListView):
    model = Articulo
    template_name = 'news/article_list.html'
    context_object_name = 'articulo'

class ArticleDetailView(DetailView):
    model = Articulo
    template_name = 'news/article_detail.html'

