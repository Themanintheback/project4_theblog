from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 27, 2018'
    },

    {
        'author': 'bob',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 27, 2020',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'about'})
