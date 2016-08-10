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

class Form_Empleados_Puesto(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('puesto_idpuesto',)
        widgets={
            'puesto_idpuesto': forms.Select(attrs={'id':'id_puesto_recomendado'})
        }

#class Form_Empleados_Estandares(forms.ModelForm):
#    class Meta:
#        model=Puesto
#        fields=('estandares_vendedor_idestandares_vendedor',)
