from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form Ingreso de mercaderia por proveedor
class Form_IngresoMercaderiaPorProveedor_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto',)

class Form_IngresoMercaderiaPorProveedor_DetalleCompra(forms.ModelForm):
    class Meta:
        model=DetalleCompra
        fields=('cantidad_compra','compra_idcompra')

class Form_IngresoMercaderiaPorProveedor_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('idtipo_producto',)

class Form_IngresoMercaderiaPorProveedor_Fotografia(forms.ModelForm):
    class Meta:
        model=Fotografia
        fields=('nombre_fotografia','ruta_fotografia',)

class Form_IngresoMercaderiaPorProveedor_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('costo_unitario_inventarioproducto','anaquel_idanaquel',)


class Form_IngresoMercaderiaPorProveedor_Anaquel(forms.ModelForm):
    class Meta:
        model=Anaquel
        fields=('bodega_idbodega',)

class Form_IngresoMercaderiaPorProveedor_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('contado_compra','proveedor_idproveedor',)
