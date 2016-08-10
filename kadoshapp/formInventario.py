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

#class Form_Inventario_Anque(forms.ModelForm):
#    class Meta:
#        model=Anaquel
#        fields=('bodega_idbodega',)

class Form_Inventario_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('bodega_idbodega',)

#class Form_Inventario_DetalleInventarioRealizado(forms.ModelForm):
#    class Meta:
#        model=DetalleInventarioRealizado
#        fields=('cantidad_real_inventario_realizado',)

class Form_Inventario_AjusteInventario(forms.ModelForm):
    class Meta:
        model=AjusteInventario
        fields=('motivo_idmotivo','empleado_idempleado','cantidad_real_ajuste',)
