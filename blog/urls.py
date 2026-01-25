from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index-page"),
    path("blog", views.blogs_view, name="blog-page"),
    path("about", views.about_view, name="about-page"),
    path("blog/<slug:slug>", views.blog_detail, name="blog-detail")
]