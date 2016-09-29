from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *
import json

#Form TrasladoMercaderia
class Form_TrasladoMerca_TrasaladoMercaderia(forms.ModelForm):
    class Meta:
        model=TrasladoMercaderia
        fields=('bodega_egreso','bodega_ingreso','motivo_idmotivo',)

class Form_TrasladoMerca_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

#class Form_TrasladoMerca_TipoProducto(forms.ModelForm):
#    class Meta:
#        model=Producto
#        fields=('marca_id_marca',)

class Form_TrasladoMerca_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)

class Form_TrasladoMerca_Cantidad(forms.Form):
    cantidad = forms.IntegerField(label='Cantidad',min_value=1)
    #widgets={
#
#    }

class FormTabla(forms.Form):
    jsonfield = forms.CharField(max_length=1024)
    def clean_jsonfield(self):
         jdata = self.cleaned_data['jsonfield']
         try:
             json_data = json.loads(jdata) #loads string as json
             #validate json_data
         except:
             raise forms.ValidationError("Invalid data in jsonfield")
         #if json data not valid:
            #raise forms.ValidationError("Invalid data in jsonfield")
         return jdata

class Form_busquedas(forms.Form):
    busqueda_producto = forms.CharField(label='Nombre promocion',max_length=100)


#class form_tabla(forms.Form):
#    inventario = forms.IntegerField(label='Inv')
#    codigo = forms.IntegerField(label='Cod')
#    cantidad = forms.IntegerField(label='Cant')
#    productoroducto = forms.CharField(label='Producto')
#    precio = models.DecimalField(label='Precio')
#    precio = models.DecimalField(label='Precio')
