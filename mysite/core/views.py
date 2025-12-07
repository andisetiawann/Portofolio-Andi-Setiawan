from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'core/index.html', {'posts': posts})
