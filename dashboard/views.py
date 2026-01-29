from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from blog_main.views import logout
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import BlogPostForm, CategoryForm, UserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import auth

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
    if not (request.user.is_staff or request.user.has_perm('blogs.add_category')):
        return HttpResponse("You are not authorized to category posts.")
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
    if not (request.user.is_staff or request.user.has_perm('blogs.delete_category')):
        return HttpResponse("You are not authorized to delete categories.")
    category = get_object_or_404(Category,id=id)
    category.delete()
    return redirect('categories')



def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

@login_required(login_url='login')
def add_post(request):
    if not (request.user.is_staff or request.user.has_perm('blogs.add_blog')):
        return HttpResponse("You are not authorized to add posts.")
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
    if not (request.user.is_staff or request.user.has_perm('blogs.change_blog')):
        return HttpResponse("You are not authorized to edit posts.")
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
    if not (request.user.is_staff or request.user.has_perm('blogs.delete_blog')):
        return HttpResponse("You are not authorized to delete posts.")
    post = get_object_or_404(Blog,id=id)
    post.delete()
    return redirect('posts')

@login_required(login_url='login')
def users(request):

    users = User.objects.all()
    context={
        'users' : users
    }

    return render(request,'dashboard/users.html',context)

def add_user(request):
    if not (request.user.is_staff or request.user.has_perm('auth.add_user')):
        return HttpResponse("You are not authorized to add users.")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {
        'form':form
    }
    return render(request,'dashboard/add_user.html',context)

def edit_user(request,id):
    if not (request.user.is_staff or request.user.has_perm('auth.change_user')):
        return HttpResponse("You are not authorized to edit users.")
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form':form,
        'user':user
    }
    return render(request,'dashboard/edit_user.html',context)

def delete_user(request,id):
    if not (request.user.is_staff or request.user.has_perm('auth.delete_user')):
        return HttpResponse("You are not authorized to delete users.")
    user = get_object_or_404(User,id=id)
    user.delete()
    return redirect('users')

def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request,'dashboard/logout.html')