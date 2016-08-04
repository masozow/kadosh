from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Empleados_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombres_persona','apellidos_persona',)

class Form_Empleados_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('puesto_idpuesto',)
