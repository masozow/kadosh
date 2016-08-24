from django import forms
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#form para fechas
class Form_Busqueda_Fechas(forms.ModelForm):
    class Meta:
        model=Precio
        exclude=('nombre_precio',)
        widgets = {
           'fechainicial_precio': forms.DateInput(attrs={'class': 'datepicker'}),
           'fechafinal_precio': forms.DateInput(attrs={'class': 'datepicker'})
        }
class Form_Busqueda_Vendedor(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('empleado_idempleado',)


class Form_Busqueda_Checkbox(forms.Form):
    checkbox_vrf=forms.BooleanField(required=False)
