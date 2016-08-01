from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form Compra
class Form_Compra_Proveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('nit_proveedor','nombre_proveedor',)
class Form_Compra_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('tipo_pago_idtipo_pago','proveedor_idproveedor','tipo_pago_idtipo_pago','casa_matriz','numero_guia','entregada_compra','empleado_recibio','vrf_compra','empleado_reviso',)
        widgets = {
            'fecha_recepcion_compra': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            'fecha_realizacion_compra': widgets.AdminDateWidget(),
            }
class Form_Compra_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto','anaquel_idanaquel','costo_unitario_inventarioproducto',)

class Form_Compra_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto',)

class Form_Compra_DetalleCompra(forms.ModelForm):
    class Meta:
        model=DetalleCompra
        fields=('cantidad_compra',)

class Form_Compra_Fotografia(forms.ModelForm):
    class Meta:
        model=Fotografia
        fields=('nombre_fotografia','ruta_fotografia',)

class Form_Compra_Anaquel(forms.ModelForm):
    class Meta:
        model=Anaquel
        fields=('bodega_idbodega',)

class Form_Compra_TipoProducto(forms.ModelForm):
    class Meta:
        model=MarcaHasTipoProducto
        fields=('marca_id_marca',)
