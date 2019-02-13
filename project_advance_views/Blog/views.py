# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import BlogForm
from .models import Blog
from django.shortcuts import render, redirect

# Create your views here.
def display_blog(request):
    blogging = Blog.objects.all()
    return render(request, 'Blog/blog_tampilan.html', {'Blogs': blogging})   

def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'Blog/blog_form.html', {'form': form})

def blog_detail(request, blog_id):
    blogging = Blog.objects.get(pk=blog_id)
    return render(request, 'Blog/blog_detail.html', {'blogging': blogging})   

