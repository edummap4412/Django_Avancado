from django.db import models
from django.db.models import Sum, F, FloatField, Max
"""

"Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Ignore for now, and let me handle existing rows with NULL myself (e.g. because you added a RunPython or RunSQL
operation to handle NULL values in a previous data migration)
 3) Quit, and let me add a default in models.py"
 
Quando esse problema aparecer : Use rm db.sqlite3

Depois :

cd "nomeaplicação"
2) ls
3) cd migrations
4) rm 00* " para apagar todos que tem 00 no inicio

"""

CHOICES = [

    ('Dev Júnior', 'Dev Júnior'),
    ('Dev Pleno', 'Dev Pleno'),
    ('Dev Senior', 'Dev Senior'),
]


class PlanoSaude(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.FloatField()

    class Meta:
        verbose_name = 'Plano de Saúde'
        verbose_name_plural = 'Planos de Saúde'

    def __str__(self):
        return f'{self.nome}'


class Registro(models.Model):
    nome = models.CharField(max_length=50, null=True, help_text='Informe seu nome completo')

    def __str__(self):
        return self.nome


class Dependentes(models.Model):
    nome = models.CharField(max_length=50, null=True, help_text='Coloque o nome do depende')

    class Meta:
        verbose_name = 'Dependente'
        verbose_name_plural = 'Dependentes'

    def __str__(self):
        return f'{self.nome}'


class Funcao(models.Model):
    nome = models.OneToOneField(Registro, null=True, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=10, choices=CHOICES)
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.PROTECT)
    depen = models.ManyToManyField(Dependentes,blank=True)
    VR = models.IntegerField()
    VT = models.IntegerField()

    def calcular_total(self):

        tot = self.funcao_set.all().aggregate(
            tot_ped=Sum((F('salario') - F('planosaude__valor')), output_field=FloatField())
        )['tot_ped']

        self.salario = tot
        self.save()

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

    def __str__(self):
        return f'{self.cargo}'






