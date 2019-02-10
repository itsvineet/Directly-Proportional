from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_name = models.ForeignKey(Post, on_delete=None)
    author = models.CharField(max_length=256, default="NO NAME")
    comment_text = models.TextField()
     

    



