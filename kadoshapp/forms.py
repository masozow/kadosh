from django import forms
from django.forms import ModelChoiceField,Select
from django.contrib.admin import widgets
from django.forms import extras

from .models import Persona,Cliente,TipoCliente
#Import para formulario de Ingres de mercaderia por Proveedor
from .models import Producto, DetalleCompra, TipoProducto, Fotografia, InventarioProducto, Anaquel, Compra
#Import para formulario de Compra
#from .models import Anaquel #, TipoProducto, Producto, Compra, InventarioProducto, DetalleCompra, Fotografia,
#impor para formulario de Punto de Venta
from .models import Venta, DetalleVenta, Promocion, Precio,Estilo, PromocionHasProducto #'''TipoProducto,''' InventarioProducto, Producto,
#import para formulario de Traslado de mercaderia
from .models import TrasladoMercaderia #'''TipoProducto''', , Producto, InventarioProducto
#impor para formulario de CierreDeCaja
from .models import CierreDeCaja, Empleado
#impor para formulario Anular Venta
#from .models import Venta, Cliente, DetalleVenta, Empleado
#import para formulario Inventario
from .models import DetalleInventarioRealizado, AjusteInventario, InventarioRealizado #Empleado, Anaquel, InventarioProducto,
#import para formulario de Promocion
#from .models import Promocion #'''Producto, TipoProducto,InventarioProducto, '''

#forms para Promocion espero ahora si aparezca
class form_Promocion_Cantidad(forms.Form):
    cantida = forms.IntegerField(label='cantidad')
class Form_Promocion_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)
class form_Promocion_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('marca_id_marca',)
class Form_Promocion_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)
class Form_Promocion_Promocion(forms.ModelForm):
    class Meta:
        model=Promocion
        fields=('nombre_promocion','valor_promocion','fecha_inicialpromocion','fecha_finalpromocion',)
#Forms para Invenario
class Form_Inventario_InventarioRealizado(forms.ModelForm):
    class Meta:
        model=InventarioRealizado
        fields=('empleado_idempleado','completo_inventario')
class Form_Inventario_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorización_empleado',)

class Form_Inventario_Anque(forms.ModelForm):
    class Meta:
        model=Anaquel
        fields=('bodega_idbodega',)

class Form_Inventario_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('anaquel_idanaquel',)

class Form_Inventario_DetalleInventarioRealizado(forms.ModelForm):
    class Meta:
        model=DetalleInventarioRealizado
        fields=('cantidad_real_inventario_realizado',)

class Form_Inventario_AjusteInventario(forms.ModelForm):
    class Meta:
        model=AjusteInventario
        fields=('motivo_idmotivo',)

#Form para Anular Venta
class Form_AnulaVenta_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('fecha_venta','idventa',)

class Form_AnulaVenta_Cliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('nit_cliente',)

class Form_AnulaVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('venta_idventa',)

class Form_AnulaVenta_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorización_empleado',)



#Form para cierre de CierreDeCaja
class Form_CierreDeCaj_CierreDeCaja(forms.ModelForm):
    class Meta:
        model=CierreDeCaja
        fields=('caja_idcaja','empleado_idempleado','total_real_cierredecaja','total_calculado_cierredecaja',)

class Form_CierreDeCaj_Empleado(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('codigo_autorización_empleado',)

#Form TrasladoMercaderia
class Form_TrasladoMerca_TrasaladoMercaderia(forms.ModelForm):
    class Meta:
        model=TrasladoMercaderia
        fields=('bodega_egreso','bodega_ingreso','motivo_idmotivo',)

class Form_TrasladoMerca_Producto(forms.ModelForm):
    class Meta:
        model=Producto
        exclude=('estado_producto','descripcion_producto',)

class Form_TrasladoMerca_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('marca_id_marca',)
class Form_TrasladoMerca_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)

class Form_TrasladoMerca_Cantidad(forms.Form):
    cantida = forms.IntegerField(label='Cantidad')


#Form Punto de Venta
class Form_PuntoVenta_busquedas(forms.Form):
    nit_del_cliente = forms.CharField(label='Buscar Nit',max_length=13)
    nombre_delapromocion = forms.CharField(label='Nombre promocion',max_length=50)
    codigo_autorizacion = forms.CharField(label='Codigo de autorización',max_length=50)

class Form_PuntoVenta_Venta(forms.ModelForm):
    class Meta:
        model=Venta
        fields=('cliente_idcliente','empleado_idempleado','tipo_pago_idtipo_pago','contado_venta',)

class Form_PuntoVenta_DetalleVenta(forms.ModelForm):
    class Meta:
        model=DetalleVenta
        fields=('cantidad_venta',)

class Form_PuntoVenta_InventarioProducto(forms.ModelForm):
    class Meta:
        model=InventarioProducto
        fields=('producto_codigo_producto',)

class Form_PuntoVenta_EstiloProducto(forms.ModelForm):
    class Meta:
        model=Estilo
        fields=('tipo_producto_idtipo_producto',)

class Form_PuntoVenta_TipoProducto(forms.ModelForm):
    class Meta:
        model=TipoProducto
        fields=('marca_id_marca',)

class Form_PuntoVenta_Producto(forms.ModelForm):
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

#Form Compra
class Form_Compra_Compra(forms.ModelForm):
    class Meta:
        model=Compra
        fields=('proveedor_idproveedor','contado_compra','tipo_pago_idtipo_pago',)

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
        model=TipoProducto
        fields=('marca_id_marca',)



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
        fields=('idtipo_producto','marca_id_marca')

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




#form Cliente
class Form_RegistroCliente_Persona(forms.ModelForm):
    class Meta:
        model=Persona
        exclude=('estado_persona',)
        #fields=('dpi_persona','nombres_persona','apellidos_persona','telefonos_persona','direccion_persona','fecha_nacimiento_persona',)
        widgets = {
            'fecha_nacimiento_persona':extras.SelectDateWidget(years=range(1900, 2015))
            #'fecha_nacimiento_persona': widgets.AdminDateWidget(), #este funcionó con todo el bloque de código que se agregó en el template
            #forms.DateInput(format='%d/%m/%Y'),
            #DateInput(attrs={'class':'datepicker'}), #Esto es para usar jquery
        }


class Form_RegistroCliente_Cliente(forms.ModelForm):
    class Meta:
        #opciones=TipoCliente.objects.filter(estado_tipocliente=1)
        model=Cliente
        exclude=('persona_idpersona','estado_cliente','fecha_registro_cliente',)
        #Personalizando las caracteristicas de los campos
        #widgets = {#widgets se utiliza para colocar ciertos controles html en lugar de textbox,
                    #como campos de fecha, radiobutton, checkbox, DropDownList(select en html), etc
                    #en este caso se utiliza un Select que sirve como DropDownList
                    #el atributo 'to_field_name' sirve como el 'combobox.value' de C#
            #'tipo_cliente_idtipo_cliente': Select( (x.idtipo_cliente, x.nombre_tipocliente) for x in opciones ),
            #Lo siguiente no funcionó
            #ModelChoiceField(queryset=TipoCliente.objects.filter(estado_tipocliente=1),to_field_name='idtipo_cliente'),#forms.ChoiceField(),
        #}
        #labels = { #Cambia las etiquetas por defecto para cada campo
        #    'tipo_cliente_idtipo_cliente': ('Tipo cliente: '),
        #}
        #help_texts = { #Muestra un texto de ayuda para el campo
        #    'tipo_cliente_idtipo_cliente': ('Elija el tipo de cliente, puede ser Mayorista, Normal, etc.'),
        #}
        #error_messages = { #Mensajes de error dependiendo de la condicion indicada
        #    'name': {
        #        'max_length': _("This writer's name is too long."),
        #    },
        #}
