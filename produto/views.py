from django.shortcuts import render
from .models import Produto
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView, View
from django.http import HttpResponse

class ProdutoCreateView (CreateView):
    model = Produto
    fields = ['descricao', 'preco']
    success_url = '/clientes/produto_form'


class ProdutoListView (ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'list_produto'


class Produtobulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maçã', 'Limao', 'Laranja', 'Pera']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)
        return HttpResponse('Funcionou')
