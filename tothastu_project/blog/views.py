from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Farhan Fuad',
        'title': 'Post 1 Title',
        'text': 'Post 1 Description',
        'post_date': '24-04-2021'
    },
    {
        'author': 'Abir',
        'title': 'Post 2 Title',
        'text': 'Post 2 Description',
        'post_date': '23-03-2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
