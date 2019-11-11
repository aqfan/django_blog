from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=250, primary_key=True)
  date = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=200)
  description = models.TextField()
  post = models.TextField(blank=False)

