import django_tables2 as tables
from .models import *

class ProductosTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    nombre_producto=tables.Column(verbose_name= 'Producto')
    codigobarras_producto=tables.Column(verbose_name= 'CodBarras')
    codigoestilo_producto=tables.Column(verbose_name= 'CodEstilo')
    marca_id_marca__nombre_marca=tables.Column(verbose_name= 'Marca')
    tipo_producto_idtipo_producto__nombre_tipoproducto=tables.Column(verbose_name= 'Tipo')
    talla_idtalla__nombre_talla=tables.Column(verbose_name= 'Talla')
    color_idcolor__nombre_color=tables.Column(verbose_name= 'Color')
    genero_idgener__nombre_genero=tables.Column(verbose_name= 'Género')
    estilo_idestilo__nombre_estilo=tables.Column(verbose_name= 'Estilo')
    cantidad_vendida=tables.Column(verbose_name= 'Cantidad Vendida')
    total_ventas=tables.Column(verbose_name= 'Total Ventas')
    class Meta:
        attrs = {'class': 'paleblue'}

class CierreTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    caja_idcaja=tables.Column(verbose_name= 'Caja')
    empleado_idempleado=tables.Column(verbose_name= 'Empleado autorizó')
    fecha_cierredecaja=tables.Column(verbose_name= 'Fecha')
    total_real_cierredecaja=tables.Column(verbose_name= 'Total contabilizado')
    total_calculado_cierredecaja=tables.Column(verbose_name= 'Total(ingresos-gastos)')
    total_efectivo_cierredecaja=tables.Column(verbose_name= 'Efectivo')
    total_cheque_cierredecaja=tables.Column(verbose_name= 'Cheque')
    total_tarjeta_cierredecaja=tables.Column(verbose_name= 'Tarjeta')
    total_egresos_cierredecaja=tables.Column(verbose_name= 'Gastos')
    finalizado_cierredecaja=tables.Column(verbose_name= 'Finalizado')
    class Meta:
        attrs = {'class': 'paleblue'}

class GastosTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    caja_idcaja=tables.Column(verbose_name= 'Caja')
    momento_gasto=tables.Column(verbose_name= 'Fecha')
    motivo_gasto=tables.Column(verbose_name= 'Motivo')
    class Meta:
        attrs = {'class': 'paleblue'}


class DevolucionTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    motivo_devolucion=tables.Column(verbose_name= 'Motivo')
    momento_devolucion=tables.Column(verbose_name= 'Fecha')
    venta_idventa=tables.Column(verbose_name= 'Venta')
    class Meta:
        attrs = {'class': 'paleblue'}


class TodosProductosTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    nombre_producto=tables.Column(verbose_name= 'Producto')
    codigobarras_producto=tables.Column(verbose_name= 'CodBarras')
    codigoestilo_producto=tables.Column(verbose_name= 'CodEstilo')
    marca_id_marca__nombre_marca=tables.Column(verbose_name= 'Marca')
    tipo_producto_idtipo_producto__nombre_tipoproducto=tables.Column(verbose_name= 'Tipo')
    talla_idtalla__nombre_talla=tables.Column(verbose_name= 'Talla')
    color_idcolor__nombre_color=tables.Column(verbose_name= 'Color')
    genero_idgener__nombre_genero=tables.Column(verbose_name= 'Género')
    estilo_idestilo__nombre_estilo=tables.Column(verbose_name= 'Estilo')
    inventarioproducto__bodega_idbodega__nombre_bodega=tables.Column(verbose_name= 'Bodega')
    inventarioproducto__existencia_actual=tables.Column(verbose_name= 'Existencias')
    class Meta:
        attrs = {'class': 'paleblue'}

class ClientesTabla(tables.Table):
    cliente_idcliente__pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    cliente_idcliente__nit_cliente=tables.Column(verbose_name= 'Nit')
    cliente_idcliente__persona_idpersona__nombres_persona=tables.Column(verbose_name= 'Nombres')
    cliente_idcliente__persona_idpersona__apellidos_persona=tables.Column(verbose_name= 'Apellidos')
    month=tables.Column(verbose_name= 'Mes')
    total_ventas=tables.Column(verbose_name= 'Total Ventas')
    class Meta:
        attrs = {'class': 'paleblue'}

class VentasTabla(tables.Table):
    vendedor_venta__persona_idpersona__nombres_persona=tables.Column(verbose_name= 'Nombres vendedor') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    vendedor_venta__persona_idpersona__apellidos_persona=tables.Column(verbose_name= 'Apellidos vendedor')
    month=tables.Column(verbose_name= 'Mes')
    total_ventas=tables.Column(verbose_name= 'Total Ventas')
    class Meta:
        attrs = {'class': 'paleblue'}

class ComprasTabla(tables.Table):
    pk=tables.Column(verbose_name= 'Cod') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    proveedor_idproveedor=tables.Column(verbose_name= 'Proveedor')
    tipo_pago_idtipo_pago=tables.Column(verbose_name= 'Tipo de pago')
    estado_compra=tables.Column(verbose_name= 'Estado de la compra')
    fecha_compra=tables.Column(verbose_name= 'Fecha en sistema')
    total_compra=tables.Column(verbose_name= 'Total')
    entregada_compra=tables.Column(verbose_name= 'Entregada')
    contado_compra=tables.Column(verbose_name= 'Se pagó al contado')
    empleado_idempleado=tables.Column(verbose_name= 'Empleado registró compra')
    numero_guia=tables.Column(verbose_name= 'No. de guía')
    vrf_compra=tables.Column(verbose_name= 'VRF')
    fecha_recepcion_compra=tables.Column(verbose_name= 'Fecha recepción mercadería')
    fecha_ralizacion_compra=tables.Column(verbose_name= 'Fecha factura compra')
    casa_matriz=tables.Column(verbose_name= 'Casa matriz')
    empleado_recibio=tables.Column(verbose_name= 'Empleado recibió mercadería')
    empleado_reviso=tables.Column(verbose_name= 'Empleado revisó mercadería')
    numero_invoice=tables.Column(verbose_name= 'No. Invoice')
    numero_factura=tables.Column(verbose_name= 'No. Factura')
    class Meta:
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
