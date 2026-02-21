from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View

from blog.models import Post, Comment
from .forms import CommentForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.

# / page
class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "blogs"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


# /blogs page
class BlogsView(ListView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = "blogs"
    ordering = ["-date"]


# /about page
class AboutView(TemplateView):
    template_name = "blog/about.html"


# /blog/post_details page
class BlogDetailView(View):

    # Custom function to check if a post is saved for later
    def is_saved_for_later(self, request, post_id):
        saved_posts = request.session.get("saved_posts")

        if saved_posts is not None:
            is_saved_for_later = post_id in saved_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        

        context = {
            "blog_detail": post,
            "form": CommentForm(),
            "is_saved_for_later": self.is_saved_for_later(request, post.id)
        }
        return render(request, "blog/blog_detail.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.post = post
            form_data.save()
            url = reverse("blog-detail", args=[slug])
            return HttpResponseRedirect(f"{url}#comment-form")

        context = {
            "blog_detail": post,
            "form": form,
            "is_saved_for_later": self.is_saved_for_later(request, post.id)
        }

        return render(request, "blog/blog_detail.html", context)


# Handle read later requests and save posts using sessions
class ReadLaterView(View):
    def get(self, request):
        saved_posts = request.session.get("saved_posts")

        context = {}
        if saved_posts is None or saved_posts == []:
            context['has_posts'] = False
        
        else:
            context['has_posts'] = True
            context['posts'] = Post.objects.filter(id__in = saved_posts)

        return render(request, "blog/read_later.html", context)

    def post(self, request):
        slug = request.POST["slug"]
        saved_posts = request.session.get("saved_posts")
        if saved_posts is None:
            saved_posts = []
        
        post_id = int(request.POST['post_id'])
        if post_id not in saved_posts:
            saved_posts.append(post_id)
        else:
            saved_posts.remove(post_id)

        request.session['saved_posts'] = saved_posts

        return HttpResponseRedirect(reverse("blog-detail", args=[slug]))
        
