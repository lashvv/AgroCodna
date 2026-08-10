from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'articles'
    )

class Video(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'videos'
    )