from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Post

def post_list(request):
    postlist = Post.objects.all() 
    #post title들 가져옴

    return render(request, 'post/post_list.html', {'postlist':postlist})


def post_write(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            contents = request.POST['contents'],
        )
        return HttpResponseRedirect(reverse('post:post_list'))
    return render(request, 'post/post_write.html')

def posting(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'post/posting.html', {'post':post})