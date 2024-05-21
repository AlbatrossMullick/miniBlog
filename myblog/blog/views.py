from django.shortcuts import render, HttpResponse
from .models import BlogPost, Comment
# from django.contrib.auth.models import User
# Create your views here.


def index(request):

    latest_blogs = BlogPost.objects.all()

    context = {
        'latest_blogs': latest_blogs,
    }

    return render(request, 'index.html', context)

