from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   

def login_user(request):
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username=username, password=password)
         
         if user is not None:
            login(request, user)
            return redirect('dashboard')
         else:
             messages.error(request, 'Username atau password salah. Silakan coba lagi.')
             return render(request, 'login.html', {'form': form})
   else:
      form = LoginForm()
      return render(request, 'login.html', {'form': form})

def logout_user(request):
   logout(request)
   return redirect('login')