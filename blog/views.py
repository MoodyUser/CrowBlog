from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from blog.forms import ContactUsForm, CreatePostForm
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


def add_new_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect(o)
    else:
        form = CreatePostForm()

    return render(request, 'contact-us.html', {
        'foo': form
    })

def update_post(request, pk):
    post = get_object_or_404(Post, id=int(pk))
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            o = form.save()
            return redirect(o)
    else:
        form = CreatePostForm(instance=post)

    return render(request, 'contact-us.html', {
        'foo': form
    })


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            mail_admins("Feedback: '{subject}' from {email}".format(**form.cleaned_data),
                        form.cleaned_data['content'])
            return redirect(reverse('home'))
    else:
        form = ContactUsForm()

    return render(request, 'contact-us.html', {
        'foo': form
    })


