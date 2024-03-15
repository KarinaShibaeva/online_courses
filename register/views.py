from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register:login')  # перенаправление на страницу авторизации

    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('siteinfo:main')  # перенаправление на главную страницу после успешной авторизации
    return render(request, 'register/login.html')

def logout_view(request):
    logout(request)
    return redirect('siteinfo:main')