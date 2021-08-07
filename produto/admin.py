from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    fields = ('descricao', 'preco')
    search_fields = ('id', 'descricao')  # usado junto com autocomplete

