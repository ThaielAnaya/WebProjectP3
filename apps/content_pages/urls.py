from django.urls import path
from .views import HomeView, page_detail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home_alt'),  # Alternative URL for home
    path('page/<slug:slug>/', page_detail, name='page_detail'),
]

