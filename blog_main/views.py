
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.models import Category,Blog
from about.models import About
from follow_us.models import FollowUs
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from utils.toast import toast

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


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request,'register.html',context)


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                #toast(request, "You have been logged in successfully.", level='success')
            return redirect('dashboard')
    form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    #toast(request, "You have been logged out successfully.", level='success')
    return redirect('home')