
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='published').order_by('updated_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html',context)