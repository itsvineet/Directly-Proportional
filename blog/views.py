from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .models import Post, Comment
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

######### SIGNUP ##########

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



#########  POST ###########
def home(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        all_comments = Comment.objects.all()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['all_comments'] = all_comments
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'


######## COMMENT ########

# Using the HTML form(Input-name values), Not Django In-Built Form
def create_comment(request, pk):
    all_comments = Comment.objects.all() 

    if request.method == "POST":
        author = request.POST.get('author')
        comment_text = request.POST.get('comment_text')
        #print(author, comment_text)
        if comment_text: # Give Author default value
            # comment_object = Comment()
            # comment_object.author = author
            # comment_object.comment_text = comment_text
            post = get_object_or_404(Post, pk=pk)
            if author == '':
                author = 'Anonymous'
            comment = Comment(post_name=post, author = author, comment_text = comment_text)
            comment.save()
            #return redirect('blog:post_detail', pk = post.pk)

    #return HttpResponseRedirect(request.path_info) 
    return redirect('blog:post_detail', pk=pk) # Calling the Post_Detail View by Passing pk value
    #return HttpResponseRedirect('/blog')

def delete_comment(request, pk):
    #comment = get_object_or_404(Comment, pk=pk)
    comment = Comment.objects.get(pk=pk)
    print(comment)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post_name.pk)




















    
