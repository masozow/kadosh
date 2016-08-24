from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *
#Forms para Invenario
#class Form_Inventario_InventarioRealizado(forms.ModelForm):
#    class Meta:
#        model=InventarioRealizado
#        fields=('empleado_idempleado','completo_inventario')

class Form_Inventario_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorizacion_empleado',)
        widgets={
            'codigo_autorizacion_empleado':forms.PasswordInput()
        }



class Form_Inventario_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('bodega_idbodega',)

class Form_Inventario_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_Inventario_AjusteInventario(forms.ModelForm):
    class Meta:
        model=AjusteInventario
        fields=('motivo_idmotivo','empleado_idempleado','cantidad_real_ajuste','inventario_producto_idinventario_producto')
