from django.shortcuts import render
from django.http import HttpResponse


blogs = [
    {
        'title': 'This is my first blog',
        'content': 'This blog is about django, we will explore the feature, uses, and scope in django in this...'
    },
    {
        'title': 'This is my second blog',
        'content': 'This blog is about django, we will explore the feature, uses, and scope in django in this...'
    },
    {
        'title': 'This is my third blog',
        'content': 'This blog is about django, we will explore the feature, uses, and scope in django in this...'
    }
]


# Create your views here.
# / page
def index(request):
    return render(request, "blog/index.html",{
            'blogs': blogs
        })

# /blogs page
# def blogs(request):
#     return render(request, "blog/blogs.html")
