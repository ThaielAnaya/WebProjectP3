from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Page
from news.models import Articulo

class HomeView(TemplateView):
    template_name = 'content_pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = get_object_or_404(Page, slug='home')
        context['latest_news'] = Articulo.objects.all().order_by('-published')[:5]
        return context

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'content_pages/page_detail.html', {'page': page})

def home(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'content_pages/home.html', {'page': page})
