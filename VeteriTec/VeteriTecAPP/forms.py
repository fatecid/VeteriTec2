from django.forms import ModelForm
from .models import Fornecedor


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['data','nome','cnpj','contato','telefone','email','descricao']

