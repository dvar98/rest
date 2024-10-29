# restaurante/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, ReservaForm, RegistroForm
from .models import Reserva, Usuario, Mesa
from .patterns.factory_method import ReservaFactory
from .patterns.singleton import ConfiguracionGlobal
from .patterns.builder import ReservaBuilder

def index_view(request):
    return render(request, 'index.html')

def login_cliente_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = authenticate(request, username=form.cleaned_data['correo'], password=form.cleaned_data['contraseña'])
            if usuario is not None:
                login(request, usuario)
                return redirect('home_cliente')
    else:
        form = LoginForm()
    return render(request, 'login_cliente.html', {'form': form})

def registro_cliente_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_cliente')
    else:
        form = RegistroForm()
    return render(request, 'registro_cliente.html', {'form': form})

def login_admin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = authenticate(request, username=form.cleaned_data['correo'], password=form.cleaned_data['contraseña'])
            if usuario is not None:
                login(request, usuario)
                return redirect('home_admin')
    else:
        form = LoginForm()
    return render(request, 'login_admin.html', {'form': form})

def registro_admin_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_admin')
    else:
        form = RegistroForm()
    return render(request, 'registro_admin.html', {'form': form})

def reserva_view(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva_builder = ReservaBuilder()
            reserva = (reserva_builder
                       .set_fecha(form.cleaned_data['fecha'])
                       .set_hora(form.cleaned_data['hora'])
                       .set_usuario(request.user)
                       .set_mesa(form.cleaned_data['mesa'])
                       .build())
            return redirect('home')
    else:
        form = ReservaForm()
    return render(request, 'reserva.html', {'form': form})

def admin_reserva_view(request):
    reservas = Reserva.objects.all()
    return render(request, 'admin_reserva.html', {'reservas': reservas})