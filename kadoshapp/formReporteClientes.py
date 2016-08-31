from django import forms
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#form para fechas
class Form_Busqueda_Fechas(forms.ModelForm):
    fechafinal_precio=forms.CharField(widget=forms.DateInput(attrs={'class': 'datepicker'}),initial=timezone.now())
    class Meta:
        model=Precio
        exclude=('nombre_precio',)
        widgets = {
           'fechainicial_precio': forms.DateInput(attrs={'class': 'datepicker'}),
           'fechafinal_precio': forms.DateInput(attrs={'class': 'datepicker'})
        }
class Form_Busqueda_Cliente(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('cliente_idcliente',)

class Form_Busqueda_Checbox(forms.Form):
    checkbo=forms.BooleanField(required=False)
