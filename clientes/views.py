from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from vendas.models import Venda
from .forms import PersonForm, ContactForm, SimpleForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView, View
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponse


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(ListView):
    template_name = 'person_list.html'
    context_object_name = 'lista_clientes'

    def get_queryset(self):
        return Person.objects.all()


class PersonDetail(DetailView):
    model = Person

    def get_object(self, queryset=None):
        """
        select_related:
        com método usado numa query em questao , no caso "doc" ,que melhora
        a performance do banco de dados. Funciona com one-to-one e ForeignKeys.
        nao funciona com Many-to-Many
        """
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(pessoa_id=self.object.id)
        return context


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name','age', 'salary', 'bio', 'photo']
    success_url = "/clientes/person_list"




class PersonUpdate(UpdateView):
    """
    criar HTML com sufixo = "nomepagina_update_form.html"
    """
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy("/clientes/person_list")


class PersonDelete(DeleteView):
    """
    crias HTML com sufixo  = "nomepagina_delete_form.html"
    """

    model = Person
    #success_url = reverse_lazy('person_list')

    def get_success_url(self):
        return reverse_lazy('person_list')


class IndexView(FormView):
    template_name = 'newindex.html'
    form_class = PersonForm
    success_url = reverse_lazy('newindex.html')


class CommentView(FormView):
    template_name = 'comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('/clientes/comment.hmtl')


