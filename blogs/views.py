from unicodedata import category
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse

from blogs.models import Blog, Category

# Create your views here.
def post_by_category(request, pk):
    posts = Blog.objects.filter(category=pk, status='published')
   # try:
    #    category = Category.objects.get(pk=pk)
    #except Category.DoesNotExist:
     #   return redirect('home')
    category = get_object_or_404(Category, pk=pk)   
    context = {
        'posts': posts,
        'category_name': category.category_name
    }
    return render(request, 'category_detail.html', context)