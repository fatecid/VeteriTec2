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


def clientesbuscar(request):
    if (request.method == "POST"):
        cliente = request.POST["cliente"]
        clie = Cliente.objects.filter(nome__icontains=cliente)
    else:
        clie = Cliente.objects.all()
    return render(request, 'clientesbuscar.html', {'clie': clie})


def clientes_update(request, id):

    clie = get_object_or_404(Cliente, pk=id)

    data = {
        'idclie': clie.id
    }

    form = ClientesForm(request.POST or None, instance=clie)
    formA = AnimalForm(request.POST or None, initial=data)


    if form.is_valid():
        form.save()
        return redirect('clientesbuscar')

    if formA.is_valid():
        formA.save()
        return redirect('clientesbuscar')

    return render(request, 'clientes.html', {'form': form ,'formA': formA})


def clientes_delete(request, id):
    clie = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        clie.delete()
        return redirect('clientesbuscar')

    return render(request, 'confirm_delete_clie.html', {'clie': clie})


def fornecedor(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'fornecedor.html', {'form': form})


def fornecedorbuscar(request):
    if (request.method == "POST"):
        fornecedor = request.POST["fornecedor"]
        forc = Fornecedor.objects.filter(nome__icontains=fornecedor)
    else:
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

    return render(request, 'confirm_delete_forc.html', {'forc': forc})


def funcionarios(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('home')
    return render(request, 'funcionarios.html', {'form': form})


def funcionariosbuscar(request):
    if (request.method == "POST"):
        funcionario = request.POST["funcionario"]
        func = Funcionario.objects.filter(nome__icontains=funcionario)
    else:
        func = Funcionario.objects.all()

    return render(request, 'funcionariosbuscar.html', {'func': func})


def funcionario_update(request, id):
        func = get_object_or_404(Funcionario, pk=id)
        form = FuncionarioForm(request.POST or None, instance=func)

        if form.is_valid():
            form.save()
            return redirect('funcionariosbuscar')

        return render(request, 'funcionarios.html', {'form': form})


def funcionario_delete(request, id):
    func = get_object_or_404(Funcionario, pk=id)

    if request.method == 'POST':
        func.delete()
        return redirect('funcionariosbuscar')

    return render(request, 'confirm_delete_func.html', {'func': func})


def relatorio(request):
    return render(request, 'relatorio.html')


def mylogout(request):
    return render(request, 'mylogout.html')
