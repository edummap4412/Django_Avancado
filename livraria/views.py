from django.shortcuts import render
from django.views.generic import View
from .models import Book , Publisher
from random import randint
from django.http import HttpResponse

class Livrobulk(View):

       # TODO: Aqui eu perciso saber como posso passar um campo "Foreign.Key" no bulk

    def get(self, request):
        livros = ['Orgulho e Preconceito', '1984',
                  'Dom Quixote de la Mancha ', 'O Pequeno Príncipe',
                  'Dom Casmurro', 'O Bandolim do Capitão Corelli'
                  'O Conde de Monte Cristo', 'Um Estudo em Vermelho']

        list_livros = []

        for livro in livros:
            l = Book(name=livro, pages=(randint(200, 500)), price=randint(49, 129), rating=randint(1, 5) ,publisher='pulisher__id')
            list_livros.append(l)

        Book.objects.bulk_create(list_livros)
        return HttpResponse('Funcionou os Livros')


class Editorbulk(View):

    def get(self, request):
        editores = ['Aleph', 'Suma', 'Editora Intrínseca', 'Grupo Editorial Record', 'Editora Rocco', 'Globo Livros', 'Darkside Books', ' Harper Collins']

        list_editores = []

        for editor in editores:
            e = Publisher(name=editor)

        Publisher.objects.bulk_create(list_editores)
        return HttpResponse('Funcionou os Autores')
