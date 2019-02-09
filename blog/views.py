from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .models import Post
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

class CreatePostView(CreateView):
    model = Post
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'



















    
