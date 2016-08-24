import django_tables2 as tables
from .models import *

class ProductosTabla(tables.Table):
    class Meta:
        model = Producto
        fields=('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','precio__valor_precio','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','cantidad_vendida','total_ventas',)
        attrs = {'class': 'paleblue'}

class ClientesTabla(tables.Table):
    class Meta:
        model = Cliente
        fields=('cliente_idcliente__pk','cliente_idcliente__nit_cliente','cliente_idcliente__persona_idpersona__nombres_persona','cliente_idcliente__persona_idpersona__apellidos_persona','month','total_ventas',)
        attrs = {'class': 'paleblue'}

class VentasTabla(tables.Table):
    class Meta:
        model = Venta
        fields=('vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona','month','total_ventas',)
        attrs = {'class': 'paleblue'}

class ComprasTabla(tables.Table):
    class Meta:
        model = Compra
        #fields=('vendedor_venta__persona_idpersona__nombres_persona','vendedor_venta__persona_idpersona__apellidos_persona','month','total_ventas',)
        attrs = {'class': 'paleblue'}
