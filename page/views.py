from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def read(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'page/read.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            content=content,
        )
        return redirect('page:read')
    else:
        return render(request, 'page/create.html')

def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'page/detail.html', context)
