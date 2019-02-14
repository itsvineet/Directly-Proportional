from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .models import Post, Comment
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
    fields = ('title', 'content',)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content',)

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/blog/login'
    template_name = 'blog/post_draft_list.html'
    context_object_name = 'draft_list'
    redirect_field_name = login_url              # Used in LoginMixin so what where should it take user if not login 
    
    def get_queryset(self):
        return Post.objects.filter(contribute__isnull=True, published_date__isnull=True).order_by('-created_date')

######## CONTRIBUTE #########

class ContributePost(CreateView):
    model = Post
    fields = ('contribute', 'title','content',)
    success_url = reverse_lazy('blog:post_list')

class ContributePostList(ListView):
    model = Post
    template_name = 'blog/contribute_manage.html'
    login_url = '/blog/login'
    context_object_name = 'draft_list'
    redirect_field_name = login_url 

    def get_queryset(self):
        return Post.objects.filter(contribute__isnull=False, published_date__isnull=True)
######## COMMENT ########

# Using the HTML form(Input-name values), Not Django In-Built Form

class PendingCommentsList(ListView):
    model = Comment
    template_name = 'blog/pending_comments.html'

    def get_queryset(self):
        return Comment.objects.filter(status = False)


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

@login_required
def delete_comment(request, pk):
    #comment = get_object_or_404(Comment, pk=pk)
    comment = Comment.objects.get(pk=pk)
    print(comment)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post_name.pk)

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    comment.save()
    return redirect('blog:post_detail', pk=comment.post_name.pk)


########### Post Publish (Publish the post by providing the publication date) ########

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    post.save()
    return redirect('blog:draft')

















    
