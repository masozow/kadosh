from django import forms
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#form para fechas
class Form_CompraEspecifica_Busqueda(forms.Form):
    numerocompra=forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))
