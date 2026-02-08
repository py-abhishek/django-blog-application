from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
import logging

logger = logging.getLogger(__name__)

# Create your views here.
# / page
def index_view(request):
    posts = Post.objects.filter(tags__in=[0, 1]).order_by('-date')[:3] # tags = 0 filter by single tag; tags__in=[0, 1] filter by multiple tags
    # posts = Post.objects.all().order_by("-date")[:3] # will create database query to get only 3 posts
    return render(request, "blog/index.html", {
        "blogs": posts
    })

# /blogs page
def blogs_view(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/blog.html",{
            'blogs': posts
        })

# /about page
def about_view(request):
    return render(request, "blog/about.html")

# /blog/post_details page
def blog_detail(request, slug):
    # blog = Post.objects.get(slug=slug)
    blog = get_object_or_404(Post, slug=slug)
    return render(request, "blog/blog_detail.html", {
        'blog_detail': blog
    })
