from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    models = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    pagenate_by = 5
    