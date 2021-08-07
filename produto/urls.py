from django.urls import path
from .views import Produtobulk, ProdutoListView, ProdutoCreateView
urlpatterns = [

    path('person_bulk/', Produtobulk.as_view(), name="person_bulk"),
    path('produto_form/', ProdutoCreateView.as_view(), name="produto_formu"),
    path('produto_list/', ProdutoListView.as_view(), name="produto_list"),

]