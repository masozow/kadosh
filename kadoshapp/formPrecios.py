from django import forms
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
        fields=('valor_precio',)
        widgets = {
            'fechainicial_precio': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            'fechafinal_precio': widgets.AdminDateWidget(),
            }
class Form_Precios_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)
