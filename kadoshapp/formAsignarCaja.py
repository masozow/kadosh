from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Gastos(forms.ModelForm):
    class Meta:
        model=Gastos
        fields=('monto_gasto','motivo_gasto','caja_idcaja',)
        widgets={
            'monto_gasto': forms.NumberInput(attrs={'min': 0})
        }
