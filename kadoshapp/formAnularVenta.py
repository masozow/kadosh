from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form para Anular Venta
class Form_AnulaVenta_busquedas(forms.Form):
    codigo_venta = forms.CharField(label='Codigo Venta',max_length=13)


class Form_AnulaVenta_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('idventa','empleado_idempleado',)
        widgets = {
            'fecha_venta': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            }

class Form_AnulaVenta_Cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nit_cliente',)

class Form_AnulaVenta_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombres_persona',)

class Form_AnulaVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('venta_idventa',)

class Form_AnulaVenta_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorización_empleado',)
