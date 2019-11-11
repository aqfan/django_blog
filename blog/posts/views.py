from django.shortcuts import render
from posts.models import Post
import markdown2

def posts(request):
  posts = Post.objects.all()
  return render(request, "posts.html", {"posts": posts})

def post_view(request, id):
  post = Post.objects.get(title=id)
  post.post = markdown2.markdown(post.post)
  return render(request, "post_view.html", {"post": post})


def author(request, id):
  posts = Post.objects.filter(author=id)
  return render(request, "posts.html", {"posts": posts})