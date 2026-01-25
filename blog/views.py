from datetime import date

from django.shortcuts import render
from django.http import HttpResponse


blogs = [
    {
        'slug': 'my-first-blog-post',
        'author': 'Abhishek Chaudhary',
        'date': date(2026, 1, 21),
        'title': 'This is my first blog',
        'excerpt': 'This blog is about django, we will explore the feature, uses, and scope in django in this...',
        'content': 'Reiciendis nulla itaque ipsum a non, rem temporibus similique at quam, officiis delectus amet quam laborum sequi ex neque, quia veritatis nulla, sit ipsa nesciunt dolorem nam provident laudantium aut odio assumenda quasi. Nesciunt animi atque assumenda, placeat architecto non velit debitis molestiae nihil, suscipit mollitia officia repellendus, quisquam velit dolore sunt rerum, illum rem voluptates ex eos animi? Ea corrupti porro distinctio quisquam consequuntur eligendi dolor, dolorem cumque nam reprehenderit repudiandae itaque ratione odit similique eveniet, nulla aspernatur quibusdam nam omnis, hic eius quam expedita?'
    },
    {
        'slug': 'my-second-blog-post',
        'author': 'Abhishek Chaudhary',
        'date': date(2026, 1, 26),
        'title': 'This is my second blog',
        'excerpt': 'This blog is about django, we will explore the feature, uses, and scope in django in this...',
        'content': 'Reiciendis nulla itaque ipsum a non, rem temporibus similique at quam, officiis delectus amet quam laborum sequi ex neque, quia veritatis nulla, sit ipsa nesciunt dolorem nam provident laudantium aut odio assumenda quasi. Nesciunt animi atque assumenda, placeat architecto non velit debitis molestiae nihil, suscipit mollitia officia repellendus, quisquam velit dolore sunt rerum, illum rem voluptates ex eos animi? Ea corrupti porro distinctio quisquam consequuntur eligendi dolor, dolorem cumque nam reprehenderit repudiandae itaque ratione odit similique eveniet, nulla aspernatur quibusdam nam omnis, hic eius quam expedita?'
    },
    {
        'slug': 'my-third-blog-post',
        'author': 'Abhishek Chaudhary',
        'date': date(2026, 1, 26),
        'title': 'This is my third blog',
        'excerpt': 'This blog is about django, we will explore the feature, uses, and scope in django in this...',
        'content': 'Reiciendis nulla itaque ipsum a non, rem temporibus similique at quam, officiis delectus amet quam laborum sequi ex neque, quia veritatis nulla, sit ipsa nesciunt dolorem nam provident laudantium aut odio assumenda quasi. Nesciunt animi atque assumenda, placeat architecto non velit debitis molestiae nihil, suscipit mollitia officia repellendus, quisquam velit dolore sunt rerum, illum rem voluptates ex eos animi? Ea corrupti porro distinctio quisquam consequuntur eligendi dolor, dolorem cumque nam reprehenderit repudiandae itaque ratione odit similique eveniet, nulla aspernatur quibusdam nam omnis, hic eius quam expedita?'
    },
    
    {
        'slug': 'my-third-blog-post',
        'author': 'Abhishek Chaudhary',
        'date': date(2026, 1, 25),
        'title': 'This is my forth blog',
        'excerpt': 'This blog is about django, we will explore the feature, uses, and scope in django in this...',
        'content': 'Reiciendis nulla itaque ipsum a non, rem temporibus similique at quam, officiis delectus amet quam laborum sequi ex neque, quia veritatis nulla, sit ipsa nesciunt dolorem nam provident laudantium aut odio assumenda quasi. Nesciunt animi atque assumenda, placeat architecto non velit debitis molestiae nihil, suscipit mollitia officia repellendus, quisquam velit dolore sunt rerum, illum rem voluptates ex eos animi? Ea corrupti porro distinctio quisquam consequuntur eligendi dolor, dolorem cumque nam reprehenderit repudiandae itaque ratione odit similique eveniet, nulla aspernatur quibusdam nam omnis, hic eius quam expedita?'
    },
]

def get_date(post):
    return post['date']


# Create your views here.
# / page
def index_view(request):
    sorted_posts = sorted(blogs, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
            'blogs': latest_posts
        })

# /blogs page
def blogs_view(request):
    return render(request, "blog/blog.html",{
            'blogs': blogs
        })

# /about page
def about_view(request):
    return render(request, "blog/about.html")

# /blog/post_details page
def blog_detail(request, slug):
    for blog in blogs:
        if blog['slug'] == slug:
            return render(request, "blog/blog_detail.html", {
                'blog_detail': blog
            })
