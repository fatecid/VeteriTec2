
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def agenda(request):
    return render(request, 'agenda.html')

def calculadora(request):
    return render(request, 'calculadora.html')

def clientes(request):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'clientes.html', {'form': form})


def fornecedor(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'fornecedor.html', {'form': form})


def funcionarios(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'funcionarios.html', {'form': form})


def relatorio(request):
    return render(request, 'relatorio.html')

def mylogout(request):
    return render(request, 'mylogout.html')
