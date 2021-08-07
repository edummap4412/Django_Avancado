from django.forms import ModelForm
from .models import Venda
from django import forms
import datetime




class VendasForm(ModelForm):

    class Meta:
        model = Venda
        CHOICES = [Venda]
        fields = ['numero', 'valor', 'desconto', 'impostos', 'pessoa']

        choice = forms.MultipleChoiceField(required=False,
                                           widget=forms.CheckboxSelectMultiple,
                                           choices=CHOICES
                                             )