from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form TrasladoMercaderia
class Form_TrasladoMerca_TrasaladoMercaderia(forms.ModelForm):
    class Meta:
        model=TrasladoMercaderia
        fields=('bodega_egreso','bodega_ingreso','motivo_idmotivo',)

class Form_TrasladoMerca_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_TrasladoMerca_TipoProducto(forms.ModelForm):
    class Meta:
        model=MarcaHasTipoProducto
        fields=('marca_id_marca',)
        
class Form_TrasladoMerca_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)

class Form_TrasladoMerca_Cantidad(forms.Form):
    cantida = forms.IntegerField(label='Cantidad')
