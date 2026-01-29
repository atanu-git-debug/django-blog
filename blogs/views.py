from unicodedata import category
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import comment as Comment
from blogs.models import Blog, Category
from django.db.models import Q
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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog,slug = slug , status = 'published')

    #comments
    comments = Comment.objects.filter(blog=single_blog)
    comments_count = comments.count()
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment_text = request.POST['comment_text']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comments_count':comments_count
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    context={
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request,'search.html',context)