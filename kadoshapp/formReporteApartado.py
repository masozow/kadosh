from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Abonos_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('venta_idventa',)

class Form_Abonos_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombres_persona','apellidos_persona')

class Form_Abonos_CuentasPorCobrar(forms.ModelForm):
    class Meta:
        model=Cuentas_por_cobrar
        fields=('idCuenta_por_cobrar','saldo_inicial_cuentaporcobrar','saldo_actual_cuentaPorCobrar')

class Form_Abonos_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('total_venta')
