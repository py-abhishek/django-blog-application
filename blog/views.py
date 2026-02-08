from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Post
import logging

logger = logging.getLogger(__name__)

# Create your views here.

# / page
class IndexView(TemplateView):
    template_name = "blog/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(tags__in=[0, 1]).order_by('-date')[:3] # tags = 0 filter by single tag; tags__in=[0, 1] filter by multiple tags
        context["blogs"] = posts
        return context


# /blogs page
class BlogsView(ListView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = "blogs"

    def get_queryset(self):
        base_query = super().get_queryset()
        blogs = base_query.order_by("-date")
        return blogs


# /about page
class AboutView(TemplateView):
    template_name = "blog/about.html"


# /blog/post_details page
class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    model = Post
    context_object_name = "blog_detail"
