from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='content_pages/home.html'), name='home'),
    path('page/<slug:slug>/', TemplateView.as_view(template_name='content_pages/page_detail.html'), name='page_detail'),
]

