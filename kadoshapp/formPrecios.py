from django import forms
from django.forms import widgets
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

class Form_Precios_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)
        
class Form_Precios_Precio(forms.ModelForm):
    class Meta:
        model=Precio
        exclude=('nombre_precio',)
        widgets = {
           'fechainicial_precio': forms.DateInput(attrs={'class': 'datepicker'}),
           'fechafinal_precio': forms.DateInput(attrs={'class': 'datepicker'})
        }
class Form_Precios_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)
