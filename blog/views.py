from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import RegisterForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

@login_required
def BLog_Main(request):
    current_user = request.user
    blog = Blog.objects.all()
    return render(request, 'blog_index.html', {'user': current_user, 'blog': blog, 'MEDIA_URL' : settings.MEDIA_URL})

def blog_create(request):
    current_user = request.user
    form = RegisterForm
    return render(request, 'blog_create.html', {'form': form, 'user': current_user})

def blog_store(request):
    if request.method =='POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request, 'Tambah Blog Berhasil')
            return redirect('blog_create')
        else:
            return render(request, 'blog_create.html', {'form' : form})

def blog_edit(request, id):
    current_user = request.user
    blog = get_object_or_404(Blog, id=id)
    form = EditForm(instance=blog)
    return render(request, 'blog_edit.html', {'blog' : blog, 'form' : form, 'user': current_user})

def blog_update(request, id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=id)
        form = EditForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.user = request.user
            form.save()
            messages.success(request, 'Edit Blog Berhasil')
            url = reverse('blog_edit', kwargs={'id': blog.id})
            return redirect(url)
        else:
            return render('blog_edit', {'form':form, 'blog': blog})
        
def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('blog')