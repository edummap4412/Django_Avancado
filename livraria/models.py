from django.db import models
from django.db.models import Max, Avg, FloatField, F, Sum

"""
Query com Annotate
  Annotate serve para pegar cada um dos campos que foram selecionados no venda_total' e soma-los com SUM, 
  Usando um slice  eu coloquei v[0] equivale a VENDA 1 na Queryset e passei .vendatotal , e consegui os valoar
  ,tambem posso pegar valoes separados como  v[0].valor e v[0].impostos
>>> v = Venda.objects.all().annotate(venda_total=Sum(F('valor') + F('impostos'), output_field=FloatField()))
>>> v
<QuerySet [<Venda: 1>, <Venda: 2>]>
>>> v[0].venda_total
60.25
>>> v[1].venda_total
72.8
>>> v[0].valor
Decimal('57.75')
>>> v[0].impostos
Decimal('2.50')

"""


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)



    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Book2(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    media = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    authors = models.ManyToManyField(Author)

    def calcula_total(self):
        total = Book2.objects.all().aggregate(media=Sum(F('price')- F('media')))['media']

        return total

    def __str__(self):
        return self.name

class Estoque(models.Model):
    quantidade = models.FloatField()
