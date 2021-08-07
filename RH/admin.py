from django.contrib import admin
from .models import Funcao, Registro, PlanoSaude, Dependentes

"""
  FUNÇÃO PARA MOSTRAR MANYTOMANY NO GRID DANDO ERRO 
 def get_depen(self, obj):
     return '. '.join([str(d) for d in obj.dependentes.all()])
 """


@admin.register(Funcao)
class FuncaoADmin(admin.ModelAdmin):
    list_display = ('cargo', 'nome', 'calcular_total')
    readonly_fields = ('salario',)


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):

    list_display = ('nome',)


@admin.register(PlanoSaude)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Dependentes)
class DependentesAdmin(admin.ModelAdmin):
    list_display = ('nome',)



