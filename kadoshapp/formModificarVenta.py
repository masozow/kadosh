from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form para Anular Venta
class Form_ModificarVenta_busquedas(forms.Form):
    codigo_venta = forms.CharField(label='Codigo Venta',max_length=13)
    precio_producto = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'True','step': '0.01','value':'0.00', 'placeholder':'0.00'}))
    cantidad_devolver=forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1}))


class Form_ModificarVenta_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('idventa','empleado_idempleado','fecha_venta')
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'class': 'datepicker'}), # widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            }

class Form_ModificarVenta_Cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nit_cliente',)

class Form_ModificarVenta_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('nombres_persona','apellidos_persona')

class Form_ModificarVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('venta_idventa','inventario_producto_idinventario_producto','cantidad_venta','valor_parcial_venta')
        widgets={
           'cantidad_venta':forms.NumberInput(attrs={'min': 1}),
           'valor_parcial_venta': forms.NumberInput(attrs={'readonly':'True','step': '0.01','value':'0.00', 'placeholder':'0.00'}),
           'inventario_producto_idinventario_producto':forms.Select(attrs={'readonly':'True'})
        }

class Form_ModificarVenta_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorizacion_empleado',)
        widgets={
            'codigo_autorizacion_empleado':forms.PasswordInput()
        }

class Form_ModificarVenta_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_ModificarVenta_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto','bodega_idbodega',)
