from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)