import django_tables2 as tables
from .models import *

class ProductosTabla(tables.Table):
    class Meta:
        model = Producto
        fields=('pk','nombre_producto','codigobarras_producto','codigoestilo_producto','marca_id_marca__nombre_marca','tipo_producto_idtipo_producto__nombre_tipoproducto','talla_idtalla__nombre_talla','color_idcolor__nombre_color','genero_idgener__nombre_genero','estilo_idestilo__nombre_estilo','cantidad_vendida','total_ventas',)
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



class RecordatorioClientesTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    persona_idpersona__nombres_persona=tables.Column(verbose_name= 'Nombres')
    persona_idpersona__apellidos_persona=tables.Column(verbose_name= 'Apellidos')
    total_ventas=tables.Column(verbose_name= 'Total compras')
    persona_idpersona__correoelectronico_persona=tables.Column(verbose_name= 'Correo electrónico')
    persona_idpersona__fecha_nacimiento_persona=tables.Column(verbose_name= 'Cumpleaños')
    tipo_cliente_idtipo_cliente__nombre_tipocliente=tables.Column(verbose_name= 'Tipo actual')
    persona_idpersona__telefonos_persona=tables.Column(verbose_name= 'Teléfonos')

class VendedoresPuestoTabla(tables.Table):
    vendedor_venta__pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    #nombre_producto=tables.Column(verbose_name= 'Nombre')
    vendedor_venta__persona_idpersona__nombres_persona=tables.Column(verbose_name= 'Nombres')
    vendedor_venta__persona_idpersona__apellidos_persona=tables.Column(verbose_name= 'Apellidos')
    total_ventas=tables.Column(verbose_name= 'Ventas mes actual')
    vendedor_venta__puesto_idpuesto__nombre_puesto=tables.Column(verbose_name = 'Puesto actual')

class ProductosSinMovimientoTabla(tables.Table):
    detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__pk=tables.Column(verbose_name= 'Cod')
    detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto=tables.Column(verbose_name= 'Nombre')
    detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigobarras_producto=tables.Column(verbose_name= 'Código de barras')
    detalleventa__inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto=tables.Column(verbose_name= 'Código de estilo')
    fecha_venta=tables.Column(verbose_name= 'Última venta')


class DetalleCompraTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    cantidad_compra=tables.Column(verbose_name= 'Cant')
    inventario_producto_idinventario_producto__producto_codigo_producto__nombre_producto=tables.Column(verbose_name= 'NombreProd')
    inventario_producto_idinventario_producto__producto_codigo_producto__codigoestilo_producto=tables.Column(verbose_name= 'CodEstilo')
    inventario_producto_idinventario_producto__producto_codigo_producto__marca_id_marca__nombre_marca=tables.Column(verbose_name= 'Marca')
    inventario_producto_idinventario_producto__producto_codigo_producto__estilo_idestilo__nombre_estilo=tables.Column(verbose_name= 'Estilo')
    inventario_producto_idinventario_producto__producto_codigo_producto__tipo_producto_idtipo_producto__nombre_tipoproducto=tables.Column(verbose_name= 'Tipo')
    inventario_producto_idinventario_producto__producto_codigo_producto__color_idcolor__nombre_color=tables.Column(verbose_name= 'Color')
    inventario_producto_idinventario_producto__producto_codigo_producto__talla_idtalla__nombre_talla=tables.Column(verbose_name= 'Talla')
    inventario_producto_idinventario_producto__producto_codigo_producto__genero_idgener__nombre_genero=tables.Column(verbose_name= 'Género')
    valor_parcial_compra=tables.Column(verbose_name= 'Valor parcial')
