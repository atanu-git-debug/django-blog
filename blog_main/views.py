
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog
from about.models import About
from follow_us.models import FollowUs

def home(request):
    
    featured_posts = Blog.objects.filter(is_featured=True,status='published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='published').order_by('updated_at')
    try:
        about_us = About.objects.get()
    except About.DoesNotExist:
        about_us = None

    
    context = {
        
        'featured_posts': featured_posts,
        'posts': posts,
        'about_us': about_us,
    }
    return render(request, 'home.html',context)