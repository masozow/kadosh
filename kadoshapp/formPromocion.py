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
        model=Producto
        fields=('marca_id_marca',)
class Form_Promocion_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)

class Form_Promocion_Precio(forms.ModelForm):
    class Meta:
        model=Precio
        fields=('valor_precio',)
        widgets = {
            'fechainicial_precio': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            'fechafinal_precio': widgets.AdminDateWidget(),
            }

class Form_Promocion_Promocion(forms.ModelForm):
    class Meta:
        model=Promocion
        fields=('nombre_promocion','valor_promocion',)
        widgets = {
            'fecha_inicialpromocion': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            'fecha_finalpromocion': widgets.AdminDateWidget(),
            }
