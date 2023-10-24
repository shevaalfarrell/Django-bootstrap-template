from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from category.models import Category
from django.urls import reverse

@login_required
def Catagory_Main(request):
    current_user = request.user
    category = Category.objects.all()
    return render(request, 'category_index.html', {'user': current_user, 'category': category})

def category_create(request):
    form = RegisterForm
    return render(request, 'category_create.html', {'form': form})

def category_store(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            nama_category = form.cleaned_data['nama_category']
            Category.objects.create(nama_category=nama_category)
            messages.success(request, 'Tambah Category Berhasil')
            return redirect('category_create')
        else:
            return render(request, 'category_create.html', {'form' : form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category')

def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    form = RegisterForm(initial={'nama_category' : category.nama_category})
    return render(request, 'category_edit.html', {'category' : category, 'form' : form})

def category_update(request,id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=id)
        form = RegisterForm(request.POST, initial={'nama_category' : category.nama_category})
        if form.is_valid():
            nama_category = form.cleaned_data['nama_category']
            category.nama_category = nama_category
            category.save()
            messages.success(request, 'Update Category Berhasil')
            url = reverse('category_edit', kwargs={'id': category.id})
            return redirect(url)
        else:
            return render('category_edit', {'form':form, 'category': category})
