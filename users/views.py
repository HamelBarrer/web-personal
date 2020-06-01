from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('commentaries:commentarie')
    template_name = 'users/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('commentaries:commentarie')
        else:
            messages.error(request, 'Usuario o Contraseña incorrectas')

    return render(request, template_name, {

    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('users:login')
