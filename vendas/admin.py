from django.contrib import admin
from .models import Venda,  ItemDoPedido
from .actions import nfe_emitida


#class ItemPedidoInline(admin.TabularInline):
class ItemPedidoInline(admin.StackedInline):
    model = ItemDoPedido
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('pessoa','calcular_total','nfe_emitida') # Esse danderline (__doc) funciona como o ponto para poder acessar o objeto de alguma ForeignKey
    list_filter = ('pessoa', ) # usar um search_fields na tabelas que contem 'pessoa' ' produtos'
    #filter_horizontal = ('produtos',)
    autocomplete_fields = ('pessoa',)
    raw_id_fields = ('pessoa',) # coloca um lupa e no campo pessoa e já pré seleciona a pessoa relacionada ao 'id'
    readonly_fields = ('valor',) # fixa o campo no caso " valor"
    actions = [nfe_emitida]
    inlines = [ItemPedidoInline]


@admin.register(ItemDoPedido)
class ItensAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'desconto')

