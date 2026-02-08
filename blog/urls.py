from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("blog", views.BlogsView.as_view(), name="blog-page"),
    path("about", views.AboutView.as_view(), name="about-page"),
    path("blog/<slug:slug>", views.BlogDetailView.as_view(), name="blog-detail")
]