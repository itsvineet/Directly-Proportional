from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView 
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    
