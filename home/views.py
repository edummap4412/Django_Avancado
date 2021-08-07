from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView, View, ListView
from django.http import HttpResponse

# TODO: Refatora para usar threades assim que possivel
def home(request):
   # import pdb; pdb.set_trace()
    value1 = 10
    value2 = 20
    res = value1 * value2
    return render(request, 'home.html', {'result': res})


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = " Teste da template View"

        return context


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Olá Mundo')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
