from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blog_count': blog_count,
    }

    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            form = CategoryForm(request.POST)
            context = {
                'form':form
            }
            return render(request,'dashboard/add_category.html',context)

    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,id):
    
    category = get_object_or_404(Category,id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context={
        'form':form,
        'category':category
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,id):
    category = get_object_or_404(Category,id=id)
    category.delete()
    return redirect('categories')



def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)#temporarily save the form data
            posts.author = request.user
            
            posts.save()#now save to database
            title = form.cleaned_data.get('title')
            posts.slug = slugify(title)+ "-"+ str(posts.id)
            posts.save()
            return redirect('posts')
        else:
            pass
    form = BlogPostForm()
    context={
        'form':form
    }
    return render(request,'dashboard/add_post.html',context)

def edit_post(request,id):
    post = get_object_or_404(Blog,id=id)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data.get('title')
            post.slug = slugify(title)+ "-"+ str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context={
        'form':form,
        'post':post
    }
    return render(request,'dashboard/edit_post.html',context)

def delete_post(request,id):
    post = get_object_or_404(Blog,id=id)
    post.delete()
    return redirect('posts')