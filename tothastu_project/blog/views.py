from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-post_date']   # for reverse ordering ['post_date']

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
