import json
import urllib
from django.conf import settings
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .models import Post, Comment
from .forms import PostForm, ContributeForm

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
    latest_post = Post.objects.filter(published_date__isnull=False).order_by("-published_date")[0:3]
    context = {
        'latest_post' : latest_post,
        'hello' : 'context variable'
    }
    
    return render(request, 'home.html', context=context)

def aboutme(request):
    return render(request, 'about_me.html')


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    ordering = '-published_date'
    paginate_by = 5
    


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        all_comments = Comment.objects.all()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['all_comments'] = all_comments
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        obj = form.save(commit=False)
        # obj.user = self.request.user
        obj.contribute = "Vineet Khandelwal"
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:draft')

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
        return Post.objects.filter(contribute="Vineet Khandelwal", published_date__isnull=True).order_by('-created_date')

######## CONTRIBUTE #########

# class ContributePost(CreateView):
   
#     form_class = ContributeForm
#     model = Post
#     success_url = reverse_lazy('blog:contribute_success')
#     success_message = 'Thanks for Contribution'


def contribute_post(request):
    
    if request.method == 'POST':
        form = ContributeForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            # recaptcha_response = request.POST.get('g-recaptcha-response')
            recaptcha_response = request.POST.get('g-recaptcha-response')
            
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'Success: Thanks for Contribution. Your Post will be listed after Review. Happy Coding :)')

            else:
                messages.error(request, 'Failed: Invalid reCAPTCHA. Please try again.')
  
            return redirect('blog:contribute')
    else:
        form = ContributeForm()

    return render(request, 'blog/post_form.html', {'form': form})
    


class ContributePostList(ListView):
    model = Post
    template_name = 'blog/contribute_manage.html'
    login_url = '/blog/login'
    context_object_name = 'draft_list'
    redirect_field_name = login_url 

    def get_queryset(self):
        return Post.objects.filter(contribute__isnull=False, published_date__isnull=True)

def contribute_success(request):
    return render(request, 'blog/contribute_success.html')

class ContributeDeleteView(PostDeleteView):
    success_url = reverse_lazy('blog:contribute_list')


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
        # austhor = request.POST.get('author')
        comment_text = request.POST.get('comment_text')

        if comment_text: # Give Author default value
            post = get_object_or_404(Post, pk=pk)
            # if author == '':
            #     author = 'Anonymous'
            comment = Comment(post_name=post, comment_text = comment_text)
            comment.save()
            

    return redirect('blog:post_detail', pk=pk) # Calling the Post_Detail View by Passing pk value
    

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

















    
