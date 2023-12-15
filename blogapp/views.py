from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import BlogPost
from .forms import PostForm
from django.urls import reverse_lazy



#create your views here.

def blog(request):
    posts = BlogPost.objects.all()
    context = {"posts" : posts}
    return render(request, "blogapp/blog.html", context)



def create_post(request):
    if request.method == "GET":
        context = {"form": PostForm()}
        return render(request, "blogapp/post_form.html", context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been successfully added.')
            return redirect('blog.html')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blogapp/post_form.html', {'form': form})
        

def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request,'blogapp/post_form.html',context)
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('blog.html')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})
        

def delete_post(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    context = {'post': post}  

    if request.method == 'GET':
        return render(request, 'blogapp/post_delete_confirm.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('blog.html')





