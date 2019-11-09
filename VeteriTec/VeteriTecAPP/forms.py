from django.forms import ModelForm
from .models import *

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['data','nome','cnpj','contato','telefone','email','descricao']


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','cpf','funcao','crmv','validade','sexo','nascimento','cep','rua','numero','bairro','cidade','uf','complemento','telefone','celular','email']


class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['data','nome','cpf','sexo','nascimento','cep','rua','numero','bairro','cidade','uf','complemento','telefone','celular','email']

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['idclie', 'nome','especie','raca','sexo','nascimento','castrado','cor','data','obs']

