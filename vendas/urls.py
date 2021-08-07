from django.urls import path
from .views import SimpleFormView, VendasCreateView, DashBoard

app_name = 'vendas'
urlpatterns = [
    path('vendas_form/', VendasCreateView.as_view(), name="venda_formu"),
    path('contact/', SimpleFormView.as_view(), name="contact_form"),
    path('dashboard/', DashBoard.as_view(), name="dashboard"),

]