from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)

########################

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)
    contribute = models.CharField(max_length=50, null=True)

    def publish(self):
        self.published_date = datetime.datetime.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:draft')
        # return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=256, default="Anonymous")
    comment_text = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    def approve(self):
        self.status = True
        self.save()


     

    



