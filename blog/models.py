from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()