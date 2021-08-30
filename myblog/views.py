from django.shortcuts import get_object_or_404, redirect, render
from blog import settings
from myblog import forms
from myblog.models import Post,Comment
from myblog.forms import PostForm,CommentForm


def list(request):
    post = Post.objects.all()
    data = {'posts':post,"BASE_URL": settings.BASE_URL}
    return render(request,'blog/list.html',data)

def post(request,id):
    post = Post.objects.filter(id=id)
    data = {'posts':post,"BASE_URL": settings.BASE_URL}
    return render(request,'blog/post.html',data)

def create(request):
    registered = False

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
            registered = True
    else:
        form = PostForm()
    data = {'registered':registered,'form':form,"BASE_URL": settings.BASE_URL}
    return render(request,'blog/create.html',data)

def edit(request,id):
    post = Post.objects.get(id=id)
    return render(request,'blog/edit.html')


def update(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST,instance=post)
    if form.is_valid():
        form.save()
        return redirect('list')
    data = {'posts':post,"BASE_URL": settings.BASE_URL}
    return render(request,'blog/post.html',data)

def delete(request,id):
    data = Post.objects.get(id=id)
    data.delete()
    return redirect('list')

##########################################
##########################################

#Comment Data

def comment(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/post')
    else:
        form = CommentForm()
        data = {'form':form,"BASE_URL": settings.BASE_URL}
        return render(request,'comment/comment.html',data)