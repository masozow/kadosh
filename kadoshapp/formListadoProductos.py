from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Listado_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_busquedas(forms.Form):
    busqueda_producto = forms.CharField(label='Nombre promocion',max_length=100)