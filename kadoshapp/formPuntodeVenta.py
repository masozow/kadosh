from django import forms
from django.contrib.admin import widgets
from django.forms import extras
from .models import *
from django.core import validators

#from django.forms import widgets
#from django.core.urlresolvers import reverse
#from django.utils.safestring import mark_safe
#from django.conf import settings

#class RelatedFieldWidgetCanAdd(widgets.Select):
#    def __init__(self, related_model, related_url=None, *args, **kw):
#        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)
#
#        if not related_url:
#            rel_to = related_model
#            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
#            related_url = 'admin:%s_%s_add' % info
#        # Be careful that here "reverse" is not allowed
#        self.related_url = related_url
#
#    def render(self, name, value, *args, **kwargs):
#        self.related_url = reverse(self.related_url)
#        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
#        output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> ' % \
#            (self.related_url, name))
#        output.append('<img src="%sadmin/img/icon_addlink.gif" width="10" height="10" alt="%s"/></a>' % (settings.STATIC_URL, 'Add Another'))
#        return mark_safe(''.join(output))





#Form Punto de Venta
class Form_PuntoVenta_busquedas(forms.Form):
    nit_del_cliente = forms.CharField(label='Buscar Nit',max_length=50)
    nombre_delapromocion = forms.CharField(label='Nombre promocion',max_length=50)
    codigo_autorizacion = forms.CharField(label='Codigo de autorización',max_length=50)

class Form_PuntoVenta_Venta(forms.ModelForm):
    #cliente_idcliente = forms.ModelChoiceField(
     #  required=False,
      # queryset=Cliente.objects.filter(estado_cliente=1),
       #widget=RelatedFieldWidgetCanAdd(Cliente, related_url="so_client_add"))
    class Meta:
        model=Venta
        fields=('anotaciones_venta','cliente_idcliente','empleado_idempleado','tipo_pago_idtipo_pago','contado_venta','vendedor_venta','caja_idcaja','es_cotizacion','total_venta')
        widgets={
            'total_venta': forms.NumberInput(attrs={'readonly':'True','step': '0.01','value':'0.00', 'placeholder':'0.00'}), #es para que no se pueda escribir en el
            'cliente_idcliente': forms.Select(attrs={'class': "browser-default"})
            #'es_cotizacion': forms.CheckboxInput(attrs={'class': 'filled-in'}) #agregando clase CSS al checkbox, ya no fue necesario, se hizo con JQuery
        }

class Form_PuntoVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('cantidad_venta','descuento_iddescuento',)
        widgets={
           'cantidad_venta':forms.NumberInput(attrs={'min': 1})
        }

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
