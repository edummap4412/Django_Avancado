from django.db.models import Avg, Min, Max, Count
from django.shortcuts import render
from .forms import VendasForm
from .models import Venda
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView, View
from django.http import HttpResponse
from django.urls import reverse_lazy


class SimpleFormView(FormView):
    template_name = 'contact.html'
    form_class = VendasForm
    success_url = reverse_lazy('/clientes/contact_form')

    def form_valid(self, form):
        form.send_email()
        return super().form_class(**self.get_form_kwargs())


class VendasCreateView(CreateView):
    model = Venda
    fields = ['numero', 'valor', 'desconto', 'desconto', 'impostos', 'pessoa', 'produtos']
    success_url = reverse_lazy('person_list')
    context_object_name = 'lista_venda'


class DashBoard(View):
    def get(self, request):

        data = {'media': Venda.objects.all().aggregate(Avg('valor'))['valor__avg'], # Esse [valor__avg] é para evitar que a chave seja mostrada no Dashboard
                'media_desconto': Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg'],
                'min': Venda.objects.all().aggregate(Min('valor'))['valor__min'],
                'max': Venda.objects.all().aggregate(Max('valor'))['valor__max'],
                'contador': Venda.objects.all().aggregate(Count('valor'))['valor__count'],
                'pedidoscom': Venda.objects.all().filter(nfe_emitida=True).aggregate(Count('id'))['id__count'],
                'pedidossem': Venda.objects.all().filter(nfe_emitida=False).aggregate(Count('id'))['id__count']

                }


        return render(request, 'dashboard.html', data)
