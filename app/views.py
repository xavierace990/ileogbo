from django.shortcuts import render,get_object_or_404
from .models import BlogPost
# Create your views here.


def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
def about(request):
    return render(request, 'about.html')