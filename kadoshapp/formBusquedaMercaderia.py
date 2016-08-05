from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Busqueda_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)
