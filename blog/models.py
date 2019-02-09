from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

# class Comment(models.Model):
#     author = models.CharField(max_length=256, default="Anonymus")
#     content = models.TextField()
     
