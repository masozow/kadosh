from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *
import json

#Form Compra
class Form_Compra_Proveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=('nit_proveedor','nombre_proveedor',)

class FormBuscar(forms.Form):
    nombre_casamatriz=forms.CharField(max_length=70)
    nit_casamatriz=forms.CharField(max_length=70)

class FormTabla(forms.Form):
    jsonfield = forms.CharField(max_length=1024)
    def clean_jsonfield(self):
         jdata = self.cleaned_data['jsonfield']
         try:
             json_data = json.loads(jdata) #loads string as json
             #validate json_data
         except Exception as e:
             raise forms.ValidationError(str(e))
         #if json data not valid:
            #raise forms.ValidationError("Invalid data in jsonfield")
         return jdata

class Form_Compra_Compra(forms.ModelForm):
    #def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
    #    super(Form_Compra_Compra, self).__init__(*args, **kwargs)
    #    self.fields['casa_matriz'].required = False
    class Meta:
        model=Compra
        fields=('tipo_pago_idtipo_pago','proveedor_idproveedor','tipo_pago_idtipo_pago','casa_matriz','numero_guia','entregada_compra','empleado_recibio','vrf_compra','empleado_reviso','fecha_recepcion_compra','fecha_realizacion_compra','total_compra','numero_invoice','numero_factura')
        widgets = {
            'total_compra': forms.NumberInput(attrs={'readonly':'True','step': '0.01','value':'0.00', 'placeholder':'0.00'}), #es para que no se pueda escribir en el
           'fecha_recepcion_compra': forms.DateInput(attrs={'class': 'datepicker'}),
           'fecha_realizacion_compra': forms.DateInput(attrs={'class': 'datepicker'})
        }

class Form_Compra_InventarioProducto(forms.ModelForm):
    def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
        # first call parent's constructor
        super(Form_Compra_InventarioProducto, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['producto_codigo_producto'].required = False

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
        fields=('cantidad_compra','valor_parcial_compra',)

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

class Form_Compra_Precio(forms.ModelForm):
    def __init__(self, *args, **kwargs):  #este codigo hace que el codigo de producto no sea necesario, así no se tiene un error de validación al no enviarlo
        super(Form_Compra_Precio, self).__init__(*args, **kwargs)
        self.fields['producto_codigo_producto'].required = False
    class Meta:
        model=Precio
        exclude=('nombre_precio',)
