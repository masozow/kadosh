from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form para cierre de CierreDeCaja
class Form_CierreDeCaj_CierreDeCaja(forms.ModelForm):
    class Meta:
        model=CierreDeCaja
        fields=('total_egresos_cierredecaja','total_efectivo_cierredecaja','total_cheque_cierredecaja','total_tarjeta_cierredecaja','caja_idcaja','empleado_idempleado','total_real_cierredecaja','total_calculado_cierredecaja',)


class Form_CierreDeCaj_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorizacion_empleado',)
