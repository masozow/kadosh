from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form Punto de Venta
class Form_PuntoVenta_busquedas(forms.Form):
    nit_del_cliente = forms.CharField(label='Buscar Nit',max_length=50)
    nombre_delapromocion = forms.CharField(label='Nombre promocion',max_length=50)
    codigo_autorizacion = forms.CharField(label='Codigo de autorización',max_length=50)

class Form_PuntoVenta_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('anotaciones_venta','cliente_idcliente','empleado_idempleado','tipo_pago_idtipo_pago','contado_venta','vendedor_venta','caja_idcaja','es_cotizacion','total_venta')
        widgets={
            'total_venta': forms.NumberInput(attrs={'readonly':'True','step': '0.01','value':'0.00', 'placeholder':'0.00'}) #es para que no se pueda escribir en el
            #'es_cotizacion': forms.CheckboxInput(attrs={'class': 'filled-in'}) #agregando clase CSS al checkbox, ya no fue necesario, se hizo con JQuery
        }

class Form_PuntoVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('cantidad_venta','descuento_iddescuento',)

class Form_PuntoVenta_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto','bodega_idbodega',)

#class Form_PuntoVenta_EstiloProducto(forms.ModelForm):
#    class Meta:
#        model=Producto
#        fields=('tipo_producto_idtipo_producto',)

#class Form_PuntoVenta_TipoProducto(forms.ModelForm):
#    class Meta:
#        model=Producto
#        fields=('marca_id_marca',)

class Form_PuntoVenta_Producto(forms.ModelForm):
    #def __init__(self, current_user, *args, **kwargs):
    #    super(Form_PuntoVenta_Producto, self).__init__(*args, **kwargs)
    #    self.fields['talla_idtalla'].queryset = self.fields['talla_idtalla'].queryset.exclude(talla_idtalla.estado_talla='0')
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_PuntoVenta_Promocion(forms.ModelForm):
    class Meta:
        model=Promocion
        fields=('idpromocion',)

class Form_PuntoVenta_PromocionHasProducto(forms.ModelForm):
    class Meta:
        model=PromocionHasProducto
        fields=('promocion_idpromocion',)


class Form_PuntoVenta_Precio(forms.ModelForm):
    class Meta:
        model=Precio
        fields=('valor_precio',)
        widgets={
            'valor_precio': forms.NumberInput(attrs={'readonly':'True'}) #es para que no se pueda escribir en el
        }

#class Form_PuntoVenta_Bodega(forms.ModelForm):
#    class Meta:
#        model=Anaquel
#        fields=('bodega_idbodega',)
