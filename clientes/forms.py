from django.forms import ModelForm
from .models import Person
from django import forms
import datetime

class ContactForm(ModelForm):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        pass


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']




BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [

    ('blues', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),

]


class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES
    )





class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'myFIELD'}))

