from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
    return render(request, 'clientes.html')

def fornecedor(request):
    return render(request, 'fornecedor.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')

def relatorio(request):
    return render(request, 'relatorio.html')

def mylogout(request):
    return render(request, 'mylogout.html')
