

from blogs.models import Blog, Category
from django import forms
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')