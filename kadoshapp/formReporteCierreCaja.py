from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form para cierre de CierreDeCaja
class Form_RepCierreCaja_CierreDeCaja(forms.ModelForm):
    class Meta:
        model=CierreDeCaja
        fields=('caja_idcaja','fecha_cierredecaja',)
        widgets = {
            'fecha_cierredecaja': forms.DateInput(attrs={'class': 'datepicker'}), # widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            }
        #total_real_cierredecaja=forms.CharField(required=True) #no sirvió para nada, no muestra que el campo es requerido
