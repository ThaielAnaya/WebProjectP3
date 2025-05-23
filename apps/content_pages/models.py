from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug =  models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'content_pages'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)