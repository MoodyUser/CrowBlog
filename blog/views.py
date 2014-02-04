from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'message': 'a < b',
    })


def single_post(request, pk):
    post = get_object_or_404(Post, id=int(pk))
    return render(request, 'post.html', {
        'post': post,
    })

def single_post_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {
        'post': post,
    })