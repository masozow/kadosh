from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *
#forms para Promocion espero ahora si aparezca
class form_Promocion_Cantidad(forms.Form):
    cantida = forms.IntegerField(label='cantidad')
class Form_Promocion_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)
class form_Promocion_TipoProducto(forms.ModelForm):
    class Meta:
        model=MarcaHasTipoProducto
        fields=('marca_id_marca',)
class Form_Promocion_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)
class Form_Promocion_Promocion(forms.ModelForm):
    class Meta:
        model=Promocion
        fields=('nombre_promocion','valor_promocion','fecha_inicialpromocion','fecha_finalpromocion',)
