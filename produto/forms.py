from .models import Produto
from django.forms import ModelForm
from django import forms


class ProdutoFrom(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco']

        def send_email(self):
            pass
