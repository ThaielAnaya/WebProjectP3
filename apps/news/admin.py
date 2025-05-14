from django.contrib import admin
from .models import Articulo

@admin.register(Articulo)
class AdminDArticulo(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
