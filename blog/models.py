from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)

########################

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



     

    



