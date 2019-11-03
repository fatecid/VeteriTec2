from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
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


def fornecedorbuscar(request):
    forc = Fornecedor.objects.all()
    return render(request, 'fornecedorbuscar.html', {'forc': forc})


def fornecedor_update(request, id):
    forc = get_object_or_404(Fornecedor, pk=id)
    form = FornecedorForm(request.POST or None, instance=forc)

    if form.is_valid():
        form.save()
        return redirect('fornecedorbuscar')

    return render(request, 'fornecedor.html' , {'form': form})

def fornecedor_delete(request, id):
    forc = get_object_or_404(Fornecedor, pk=id)

    if request.method == 'POST':
        forc.delete()
        return redirect('fornecedorbuscar')

    return render(request, 'confirm_delete.html', {'forc': forc})


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
