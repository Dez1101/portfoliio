from django.shortcuts import render
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/blogs.html', {'blogs': blogs})