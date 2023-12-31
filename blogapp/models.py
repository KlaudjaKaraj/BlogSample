from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='Write your content here...')
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']
