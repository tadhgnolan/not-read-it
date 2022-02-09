from django.shortcuts import render
from .models import Post


def get_posts(request):
    posts = Post.objects.all()
    template = "readit/posts.html"
    context = {
        "posts": posts,
    }
    return render(request, template, context)