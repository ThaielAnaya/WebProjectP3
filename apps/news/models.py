from django.db import models
from django.urls import reverse

class Articulo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("news:detail", args=[self.slug])
    
