from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Abonos_busquedas(forms.Form):
    codigo_venta = forms.CharField(label='Codigo Venta',max_length=13)


class Form_Abonos_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('idventa','fecha_venta')
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'class': 'datepicker'}), # widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            }

class Form_Abonos_Cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nit_cliente',)

class Form_Abonos_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombres_persona','apellidos_persona')

class Form_Abonos_PagosCuentasPorCobrar(forms.ModelForm):
    class Meta:
        model=PagosCuentaPorCobrar
        fields=('monto_pago_cuentaporcobrar','tipo_pago_idtipo_pago')
class Form_Abonos_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('venta_idventa',)
