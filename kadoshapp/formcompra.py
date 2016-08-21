from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *

#Form Compra
class Form_Compra_Proveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('nit_proveedor','nombre_proveedor',)

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

class Form_Compra_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('tipo_pago_idtipo_pago','proveedor_idproveedor','tipo_pago_idtipo_pago','casa_matriz','numero_guia','entregada_compra','empleado_recibio','vrf_compra','empleado_reviso','fecha_recepcion_compra','fecha_realizacion_compra',)
        widgets = {
           'fecha_recepcion_compra': forms.DateInput(attrs={'class': 'datepicker'}),
           'fecha_realizacion_compra': forms.DateInput(attrs={'class': 'datepicker'})
        }

class Form_Compra_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto','costo_unitario_inventarioproducto','bodega_idbodega',)

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
        fields=('idfotografia','ruta_fotografia','nombre_fotografia','estado_fotografia','principal_fotografia')

#class Form_Compra_Anaquel(forms.ModelForm):
#    class Meta:
#        model=Anaquel
#        fields=('bodega_idbodega',)

class Form_Compra_TipoProducto(forms.ModelForm):
    class Meta:
        model=Producto
        fields=('marca_id_marca',)
