from datetime import datetime
from django import template
from django.template.defaultfilters import stringfilter, floatformat
from django.utils.safestring import SafeString

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)


# Criei uma stringfilter

@register.filter
@stringfilter # esse decorator é usado para quando passar numeros na string ele nao de Attribute.Error por conta do metodo lower()
def lower(value):
    return value.lower()


@register.filter
def arredonda(value, casas):
    return round(value, casas)


@register.simple_tag
@stringfilter
def footer_message():
    return "Aprendendo Django Avançado"


@floatformat
def float():
    return floatformat
