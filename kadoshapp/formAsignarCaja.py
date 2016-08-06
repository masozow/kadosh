from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Asignar_CajaHasEmpleado(forms.ModelForm):
    class Meta:
        model=CajaHasEmpleado
        fields=('caja_idcaja','empleado_idempleado',)
