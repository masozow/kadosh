from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.utils.timezone import localtime, now
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.



class AjusteInventario(models.Model):
    idajuste_inventario = models.AutoField(db_column='idAjuste_inventario', primary_key=True)  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    motivo_idmotivo = models.ForeignKey('Motivo', db_column='Motivo_idMotivo')  # Field name made lowercase.
    fecha_horaajuste = models.DateTimeField(db_column='fecha_horaAjuste', default=timezone.now)  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado',blank=True,null=True)
    cantidad_real_ajuste = models.IntegerField()

    def __str__(self):
        return '%s) %s' % (self.idajuste_inventario,self.inventario_producto_idinventario_producto)

    class Meta:
        managed = True
        db_table = 'Ajuste_inventario'


#class Anaquel(models.Model):
#    idanaquel = models.AutoField(db_column='idAnaquel', primary_key=True)  # Field name made lowercase.
#    bodega_idbodega = models.ForeignKey('Bodega', db_column='Bodega_idBodega')  # Field name made lowercase.
#    codigo_anaquel = models.CharField(max_length=45, blank=True, null=True,unique=True)
#    estado_anaquel = models.BooleanField(default=True)  # This field type is a guess.
#
#    def __str__(self):
#        return '%s (%s)' % (self.codigo_anaquel,self.bodega_idbodega.nombre_bodega)
#
#    class Meta:
#        managed = True
#        db_table = 'Anaquel'


class Bodega(models.Model):
    idbodega = models.AutoField(db_column='idBodega', primary_key=True)  # Field name made lowercase.
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    nombre_bodega = models.CharField(max_length=45, blank=True, null=True)
    descripcion_bodega = models.CharField(max_length=100, blank=True, null=True)
    estado_bodega = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_bodega

    class Meta:
        managed = True
        db_table = 'Bodega'


class Caja(models.Model):
    idcaja = models.AutoField(db_column='idCaja', primary_key=True)  # Field name made lowercase.
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    descripcion_caja = models.CharField(max_length=45, blank=True, null=True)
    estado_caja = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.idcaja,self.descripcion_caja)

    class Meta:
        managed = True
        db_table = 'Caja'


class CajaHasEmpleado(models.Model):
    idcaja_has_empleado = models.AutoField(db_column='idcaja_has_empleado', primary_key=True)  # Field name made lowercase.
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado')  # Field name made lowercase.
    momento_asignacion_caja = models.DateTimeField(default=timezone.now)
    momento_desasignacion_caja = models.DateTimeField(blank=True, null=True)
    estado_asignacion_caja = models.BooleanField(db_column='estado_asignación_caja', default=True)

    def __str__(self):
        return 'Caja: %s - Fecha: %s - Empleado: %s' % (self.caja_idcaja, self.momento_asignacion_caja, self.empleado_idempleado)

    class Meta:
        managed = True
        db_table = 'Caja_has_Empleado'

class CierreDeCaja(models.Model):
    idcierre_de_caja = models.AutoField(db_column='idCierre_de_caja', primary_key=True)  # Field name made lowercase.
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado')  # Field name made lowercase.
    fecha_cierredecaja = models.DateField(db_column='fecha_cierreDeCaja', default=timezone.now)  # Field name made lowercase.
    total_real_cierredecaja = models.DecimalField(db_column='total_real_cierreDeCaja', max_digits=12, decimal_places=2)  # Field name made lowercase.
    total_calculado_cierredecaja = models.DecimalField(db_column='total_calculado_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finalizado_cierredecaja = models.BooleanField(db_column='finalizado_cierreDeCaja', default=True)
    total_efectivo_cierredecaja = models.DecimalField(db_column='total_efectivo_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_cheque_cierredecaja = models.DecimalField(db_column='total_cheque_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_tarjeta_cierredecaja = models.DecimalField(db_column='total_tarjeta_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_egresos_cierredecaja = models.DecimalField(db_column='total_egresos_cierreDeCaja', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return 'Caja: %s - Fecha: %s' % (self.caja_idcaja, self.fecha_cierredecaja)

    class Meta:
        managed = True
        db_table = 'Cierre_de_caja'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    #usuario = models.ForeignKey('auth.User')
    persona_idpersona = models.ForeignKey('Persona', db_column='Persona_idPersona')  # Field name made lowercase.
    nit_cliente = models.CharField(max_length=13, blank=True, null=True)
    tipo_cliente_idtipo_cliente = models.ForeignKey('TipoCliente', db_column='Tipo_cliente_idTipo_cliente')  # Field name made lowercase.
    estado_cliente = models.BooleanField(default=True)
    fecha_registro_cliente = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s [%s %s]' % (self.nit_cliente, self.persona_idpersona.nombres_persona, self.persona_idpersona.apellidos_persona)

    class Meta:
        managed = True
        ordering = ["persona_idpersona"]
        db_table = 'Cliente'


class Color(models.Model):
    idcolor = models.AutoField(db_column='idColor', primary_key=True)  # Field name made lowercase.
    nombre_color = models.CharField(max_length=45)
    estado_color = models.BooleanField(default=True)  # This field type is a guess.

    def __str__(self):
        return self.nombre_color

    class Meta:
        managed = True
        ordering=["nombre_color"]
        db_table = 'Color'


#class Combo(models.Model):
#    idcombo = models.AutoField(db_column='idCombo', primary_key=True)  # Field name made lowercase.
#    nombre_combo = models.CharField(max_length=45, blank=True, null=True)
#    estado_combo = models.BooleanField(default=True)
#
#    def __str__(self):
#        return self.nombre_combo
#
#    class Meta:
#        managed = True
#        db_table = 'Combo'


class Compra(models.Model):
    idcompra = models.AutoField(db_column='idCompra', primary_key=True)  # Field name made lowercase.
    proveedor_idproveedor = models.ForeignKey('Proveedor', db_column='Proveedor_idProveedor',related_name='proveedor_proveedor_idproveedor')  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey('TipoPago', db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.
    estado_compra = models.BooleanField(default=True)
    fecha_compra = models.DateTimeField(default=timezone.now)
    total_compra = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    entregada_compra = models.BooleanField(default=True)
    contado_compra = models.BooleanField(default=True)
    empleado_idempleado = models.ForeignKey('Empleado', db_column='Empleado_idEmpleado',related_name='empleado_empleado_idempleado')  # Field name made lowercase.
    numero_guia = models.CharField(max_length=45, blank=True, null=True)
    vrf_compra = models.BooleanField(default=True)
    fecha_recepcion_compra = models.DateField(default=timezone.now)
    fecha_realizacion_compra = models.DateField(default=timezone.now)
    casa_matriz = models.ForeignKey('Proveedor', db_column='Casa_matriz',related_name='proveedor_casa_matriz',blank=True,null=True)  # Field name made lowercase.
    empleado_recibio = models.ForeignKey('Empleado', db_column='Empleado_recibio',related_name='empleado_empleado_recibio',blank=True,null=True)  # Field name made lowercase.
    empleado_reviso = models.ForeignKey('Empleado', db_column='Empleado_reviso',related_name='empleado_empleado_reviso',blank=True,null=True)  # Field name made lowercase.
    numero_invoice = models.CharField(max_length=45, blank=True, null=True)
    numero_factura = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return 'Compra: %s - Proveedor: %s  - Fecha: %s' % (self.idcompra, self.proveedor_idproveedor.nombre_proveedor, self.fecha_compra)

    class Meta:
        managed = True
        db_table = 'Compra'


class Contacto(models.Model):
    idcontacto = models.AutoField(db_column='idContacto', primary_key=True)  # Field name made lowercase.
    correo_contacto = models.CharField(max_length=45, blank=True, null=True)
    nombre_contacto = models.CharField(max_length=50, blank=True, null=True)
    asunto_contacto = models.CharField(max_length=60, blank=True, null=True)
    mensaje_contacto = models.CharField(max_length=400, blank=True, null=True)
    estado_contacto = models.BooleanField(default=True)
    fecha_contacto = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Nombre: %s - Asunto: %s  - Fecha: %s' % (self.nombre_contacto, self.asunto_contacto, self.fecha_contacto)

    class Meta:
        managed = True
        db_table = 'Contacto'


class Contenido(models.Model):
    idcontenido = models.AutoField(db_column='idContenido', primary_key=True)  # Field name made lowercase.
    resumen_contenido = models.CharField(max_length=45, blank=True, null=True)
    texto_contenido = models.CharField(max_length=100, blank=True, null=True)
    index_idindex = models.ForeignKey('Index', db_column='Index_idIndex')  # Field name made lowercase.
    estado_contenido = models.BooleanField(default=True)

    def __str__(self):
        return 'Contenido: %s - Resumen: %s ' % (self.idcontenido, self.resumen_contenido)

    class Meta:
        managed = True
        db_table = 'Contenido'


class CuentaPorCobrar(models.Model):
    idcuenta_por_cobrar = models.AutoField(db_column='idCuenta_por_cobrar', primary_key=True)  # Field name made lowercase.
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    saldo_inicial_cuentaporcobrar = models.DecimalField(db_column='saldo_inicial_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo_actual_cuentaporcobrar = models.DecimalField(db_column='saldo_actual_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_pagofinal_cuentaporcobrar = models.DateField(db_column='fecha_pagoFinal_cuentaPorCobrar', blank=True, null=True)  # Field name made lowercase.
    estado_cuentaporcobrar = models.BooleanField(db_column='estado_cuentaPorCobrar', default=True)  # Field name made lowercase.

    def __str__(self):
        return 'Cuenta: %s - Venta: %s ' % (self.idcuenta_por_cobrar, self.venta_idventa.idventa)

    class Meta:
        managed = True
        db_table = 'Cuenta_por_cobrar'


class CuentaPorPagar(models.Model):
    idcuenta_por_pagar = models.AutoField(db_column='idCuenta_por_pagar', primary_key=True)  # Field name made lowercase.
    compra_idcompra = models.ForeignKey(Compra, db_column='Compra_idCompra')  # Field name made lowercase.
    saldo_inicial_cuentaporpagar = models.DecimalField(db_column='saldo_inicial_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saldo_actual_cuentaporpagar = models.DecimalField(db_column='saldo_actual_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha_pagofinal_cuentaporpagar = models.DateField(db_column='fecha_pagofinal_cuentaPorPagar', blank=True, null=True)  # Field name made lowercase.
    estado_cuentaporpagar = models.BooleanField(db_column='estado_cuentaPorPagar', default=True)  # Field name made lowercase.

    def __str__(self):
        return 'Cuenta: %s - Compra: %s ' % (self.idcuenta_por_pagar, self.compra_idcompra.idcompra)

    class Meta:
        managed = True
        db_table = 'Cuenta_por_pagar'


class DatosEnvio(models.Model):
    iddatos_envio = models.AutoField(db_column='idDatos_envio', primary_key=True)  # Field name made lowercase.
    nombres_envio = models.CharField(max_length=80, blank=True, null=True)
    apellidos_envio = models.CharField(max_length=80, blank=True, null=True)
    correo_electronico_envio = models.CharField(max_length=60, blank=True, null=True)
    telefonos_envio = models.CharField(max_length=36, blank=True, null=True)
    envio_idenvio = models.ForeignKey('Envio', db_column='Envio_idEnvio')  # Field name made lowercase.

    def __str__(self):
        return 'Envio: %s - Nombre: %s %s' % (self.envio_idenvio, self.nombres_envio,self.apellidos_envio)

    class Meta:
        managed = True
        db_table = 'Datos_envio'

class Descuento(models.Model):
    iddescuento = models.AutoField(db_column='idDescuento', primary_key=True)  # Field name made lowercase.
    descripcion_descuento = models.CharField(max_length=60, blank=True, null=True)
    monto_descuento = models.DecimalField(db_column='monto_descuento', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentaje_descuento = models.BooleanField(db_column='porcentaje_descuento', default=False)
    estado_descuento = models.BooleanField(db_column='estado_descuento', default=True)
    autorizado_descuento = models.BooleanField(db_column='autorizado_descuento', default=False)

    def __str__(self):
        return '%s-%s-%s' % (self.iddescuento, self.descripcion_descuento,self.monto_descuento)

    class Meta:
        managed = True
        db_table = 'Descuento'


#class DetalleInventarioRealizado(models.Model):
#    inventario_realizado_idinventario_realizado = models.ForeignKey('InventarioRealizado', db_column='Inventario_realizado_idInventario_realizado')  # Field name made lowercase.
#    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
#    ajuste_inventario_idajuste_inventario = models.ForeignKey(AjusteInventario, db_column='Ajuste_inventario_idAjuste_inventario', null=True, blank=True)  # Field name made lowercase.
#    cantidad_real_inventario_realizado = models.IntegerField(blank=True, null=True)
#    iddetalleinventariorealizado = models.AutoField(db_column='iddetalleinventariorealizado', primary_key=True)
#
#    def __str__(self):
#        return '%s - Lote de producto: %s' % (self.inventario_realizado_idinventario_realizado, self.inventario_producto_idinventario_producto.idinventario_producto)
#
#    class Meta:
#        managed = True
#        db_table = 'Detalle inventario_realizado'


class DetalleCompra(models.Model):
    compra_idcompra = models.ForeignKey(Compra, db_column='Compra_idCompra')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    cantidad_compra = models.IntegerField(blank=True, null=True)
    valor_parcial_compra = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    iddetallecompra = models.AutoField(db_column='idDetalleCompra', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return ' %s - Producto: %s - Detalle: %s' % (self.compra_idcompra, self.inventario_producto_idinventario_producto,self.iddetallecompra)

    class Meta:
        managed = True
        db_table = 'Detalle_compra'


class DetalleVenta(models.Model):
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey('InventarioProducto', db_column='Inventario_producto_idInventario_producto',blank=True,null=True)  # Field name made lowercase.
    cantidad_venta = models.IntegerField(blank=True, null=True)
    valor_parcial_venta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    iddetalleventa = models.AutoField(db_column='idDetalleVenta', primary_key=True)  # Field name made lowercase.
    descuento_iddescuento = models.ForeignKey(Descuento, db_column='Descuento_idDescuento',blank=True,null=True)  # Field name made lowercase.
    promocion_idpromocion = models.ForeignKey('Promocion', db_column='Promocion_idPromocion',blank=True,null=True)  # Field name made lowercase.

    def __str__(self):
        return 'Id: %s - Venta: %s - Inv: %s ' % (self.iddetalleventa,self.venta_idventa.idventa, self.inventario_producto_idinventario_producto )

    class Meta:
        managed = True
        db_table = 'Detalle_venta'


class Devolucion(models.Model):
    iddevoucion = models.AutoField(db_column='idDevolucion', primary_key=True)  # Field name made lowercase.
    motivo_devolucion = models.CharField(max_length=100, blank=True, null=True)
    momento_devolucion = models.DateTimeField(default=timezone.now)
    involucra_cambiodevolucion = models.BooleanField(default=True)
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.

    def __str__(self):
        return '%s - Venta: %s' % (self.iddevolucion,self.venta_idventa.idventa)

    class Meta:
        managed = True
        db_table = 'Devolucion'

class Empleado(models.Model):
    idempleado = models.AutoField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', db_column='Persona_idPersona')  # Field name made lowercase.
    puesto_idpuesto = models.ForeignKey('Puesto', db_column='Puesto_idPuesto')  # Field name made lowercase.
    estado_empleado = models.BooleanField(default=True)
    fecha_contratacion_empleado = models.DateField(default=timezone.now)
    codigo_autorizacion_empleado = models.CharField(max_length=45, blank=True, null=True)
    sucursal_idsucursal = models.ForeignKey('Sucursal', db_column='Sucursal_idSucursal')  # Field name made lowercase.
    fecha_baja_empleado = models.DateField(blank=True,null=True)
    motivo_baja_empleado = models.CharField(max_length=200, blank=True, null=True)
    fotografia_empleado = models.ImageField(upload_to = '')
    auth_user = models.ForeignKey('auth.User')

    def __str__(self):
        return '%s - %s %s' % (self.idempleado, self.persona_idpersona.nombres_persona,self.persona_idpersona.apellidos_persona)

    class Meta:
        managed = True
        db_table = 'Empleado'


class Envio(models.Model):
    idenvio = models.AutoField(db_column='idEnvio', primary_key=True)  # Field name made lowercase.
    venta_idventa = models.ForeignKey('Venta', db_column='Venta_idVenta')  # Field name made lowercase.
    repartidor_envio = models.CharField(max_length=50, blank=True, null=True)
    salida_envio = models.BooleanField(default=False)
    encamino_envio = models.BooleanField(db_column='enCamino_envio', default=False)  # Field name made lowercase.
    entregado_envio = models.BooleanField(default=False)
    estado_envio = models.BooleanField(default=True)
    momentosolicitud_envio = models.DateTimeField(db_column='momentoSolicitud_envio', default=timezone.now)  # Field name made lowercase.

    def __str__(self):
        return '%s - Rep: %s - F: %s' % (self.idenvio, self.repartidor_envio,self.momentosolicitud_envio)

    class Meta:
        managed = True
        db_table = 'Envio'


#class EstandarCliente(models.Model):
#    idestandarcliente = models.AutoField(db_column='idEstandarCliente', primary_key=True)  # Field name made lowercase.
#    categoria_cliente = models.CharField(max_length=45, blank=True, null=True)
#    comprasminimas_cliente = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#    estado_estandarcliente = models.BooleanField(default=True)
#
#    def __str__(self):
#        return '%s' % (self.categoria_cliente)
#
#    class Meta:
#        managed = True
#        db_table = 'EstandarCliente'


#class EstandaresVendedor(models.Model):
#    idestandares_vendedor = models.AutoField(db_column='idEstandares_vendedor', primary_key=True)  # Field name made lowercase.
#    categoria_vendedor = models.CharField(max_length=45, blank=True, null=True)
#    ventasminimas_vendedor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#    estado_estandarvendedor = models.BooleanField(default=True)
#
#    def __str__(self):
#        return '%s' % (self.categoria_vendedor)
#
#    class Meta:
#        managed = True
#        db_table = 'Estandares_vendedor'


class Estilo(models.Model):
    idestilo = models.AutoField(db_column='idEstilo', primary_key=True)  # Field name made lowercase.
    nombre_estilo = models.CharField(max_length=45)
    estado_estilo = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.nombre_estilo)

    class Meta:
        managed = True
        ordering=["nombre_estilo"]
        db_table = 'Estilo'


class Fotografia(models.Model):
    idfotografia = models.AutoField(db_column='idFotografia', primary_key=True)  # Field name made lowercase.
    nombre_fotografia = models.CharField(max_length=45, blank=True, null=True,default='s/n')
    ruta_fotografia = models.ImageField(upload_to = '') #settings.MEDIA_ROOT
    estado_fotografia = models.BooleanField(default=True)
    principal_fotografia = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.idfotografia, self.nombre_fotografia)

    class Meta:
        managed = True
        db_table = 'Fotografia'


class Gastos(models.Model):
    idgastos = models.AutoField(db_column='idGastos', primary_key=True)  # Field name made lowercase.
    monto_gasto = models.DecimalField(max_digits=12, decimal_places=2)
    motivo_gasto = models.CharField(max_length=60)
    momento_gasto = models.DateTimeField(default=timezone.now)
    caja_idcaja = models.ForeignKey('Caja', db_column='Caja_idCaja')

    def __str__(self):
        return '%s - %s' % (self.motivo_gasto,self.monto_gasto)

    class Meta:
        managed = True
        db_table = 'Gastos'


class Genero(models.Model):
    idgener = models.AutoField(db_column='idGener', primary_key=True)  # Field name made lowercase.
    nombre_genero = models.CharField(max_length=45)
    estado_genero = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.nombre_genero)

    class Meta:
        managed = True
        ordering=["nombre_genero"]
        db_table = 'Genero'


class Index(models.Model):
    idindex = models.AutoField(db_column='idIndex', primary_key=True)  # Field name made lowercase.
    titulo_index = models.CharField(max_length=60, blank=True, null=True)
    parrafo_index = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.idindex, self.titulo_index)

    class Meta:
        managed = True
        db_table = 'Index'


class IndexHasFotografia(models.Model):
    index_idindex = models.ForeignKey(Index, db_column='Index_idIndex')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey(Fotografia, db_column='Fotografia_idFotografia')  # Field name made lowercase.
    ubicacion_fotografiaindex = models.SmallIntegerField(db_column='ubicacion_fotografiaIndex', blank=True, null=True)  # Field name made lowercase.
    idindexhasfotografia = models.AutoField(db_column='idindexhasfotografia', primary_key=True)

    def __str__(self):
        return '%s - Index:%s - Foto: %s' % (self.idindexhasfotografia,self.index_idindex, self.fotografia_idfotografia)

    class Meta:
        managed = True
        db_table = 'Index_has_Fotografia'
        unique_together = (('index_idindex', 'fotografia_idfotografia'),)


class InventarioProducto(models.Model):
    idinventario_producto = models.AutoField(db_column='idInventario_producto', primary_key=True)  # Field name made lowercase.
    existencia_minima = models.IntegerField(blank=True, null=True)
    existencia_maxima = models.IntegerField(blank=True, null=True)
    existencia_actual = models.IntegerField(blank=True, null=True)
    estado_inventario_producto = models.BooleanField(default=True)
    bodega_idbodega = models.ForeignKey(Bodega, db_column='bodega_idbodega')  # Field name made lowercase.
    fecha_creacioninventario = models.DateTimeField(db_column='fecha_creacionInventario', default=timezone.now)  # Field name made lowercase.
    producto_codigo_producto = models.ForeignKey('Producto', db_column='Producto_codigo_producto')  # Field name made lowercase.
    costo_unitario_inventarioproducto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    #quitar el campo de arriba en cuanto se empiece a trabajar con compra
    def __str__(self):
        return '%s - P: %s - F: %s ' % (self.idinventario_producto, self.producto_codigo_producto, self.fecha_creacioninventario)

    class Meta:
        managed = True
        db_table = 'Inventario_producto'


#class InventarioRealizado(models.Model):
#    idinventario_realizado = models.AutoField(db_column='idInventario_realizado', primary_key=True)  # Field name made lowercase.
#    fecha_realizacion_inventario = models.DateTimeField(default=timezone.now)
#    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado')  # Field name made lowercase.
#    completo_inventario = models.BooleanField()
#    estado_inventario = models.BooleanField(default=True)
#
#    def __str__(self):
#        return 'Id: %s - F: %s' % (self.idinventario_realizado, self.fecha_realizacion_inventario)

#    class Meta:
#        managed = True
#        db_table = 'Inventario_realizado'


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=50)
    estado_marca = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.nombre_marca)

    class Meta:
        managed = True
        ordering=["nombre_marca"]
        db_table = 'Marca'


#class MarcaHasTipoProducto(models.Model):
#    marca_id_marca = models.ForeignKey('Marca', db_column='Marca_id_marca')  # Field name made lowercase.
#    tipo_producto_idtipo_producto = models.ForeignKey('TipoProducto', db_column='Tipo_producto_idTipo_producto')  # Field name made lowercase.
#    idmarcahastipopoducto = models.AutoField(db_column='idMarcaHasTipoPoducto', primary_key=True)
#
#    def __str__(self):
#        return '%s - %s' % (self.marca_id_marca, self.tipo_producto_idtipo_producto)
#
#    class Meta:
#        managed = True
#        db_table = 'Marca_has_Tipo_producto'


class Motivo(models.Model):
    idmotivo = models.AutoField(db_column='idMotivo', primary_key=True)  # Field name made lowercase.
    nombre_motivo = models.CharField(max_length=60, blank=True, null=True)
    estado_motivo = models.BooleanField(default=True)
    traslado_motivo = models.BooleanField()

    def __str__(self):
        return '%s - %s' % (self.idmotivo, self.nombre_motivo)

    class Meta:
        managed = True
        db_table = 'Motivo'


class Noticia(models.Model):
    idnoticia = models.AutoField(db_column='idNoticia', primary_key=True)  # Field name made lowercase.
    momento_publicacion_noticia = models.DateTimeField(default=timezone.now)
    titulo_noticia = models.CharField(max_length=70, blank=True, null=True)
    contenido_noticia = models.CharField(max_length=600, blank=True, null=True)
    estado_noticia = models.BooleanField(default=True)

    def __str__(self):
        return '%s - F: %s - %s' % (self.idnoticia, self.momento_publicacion_noticia,self.titulo_noticia[0:15])

    class Meta:
        managed = True
        db_table = 'Noticia'


class NoticiaHasFotografia(models.Model):
    noticia_idnoticia = models.ForeignKey('Noticia', db_column='Noticia_idNoticia')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey('Fotografia', db_column='Fotografia_idFotografia')  # Field name made lowercase.
    vista_previa = models.BooleanField(default=False)
    idnoticiahasfotografia = models.AutoField(db_column='idnoticiahasfotografia', primary_key=True)

    def __str__(self):
        return 'N: %s - Fo: %s' % (self.noticia_idnoticia, self.fotografia_idfotografia)

    class Meta:
        managed = True
        db_table = 'Noticia_has_Fotografia'
        unique_together = (('noticia_idnoticia', 'fotografia_idfotografia'),)


class PagoCuentaPorPagar(models.Model):
    idpago_cuenta_por_pagar = models.AutoField(db_column='idPago_cuenta_por_pagar', primary_key=True)  # Field name made lowercase.
    cuenta_por_pagar_idcuenta_por_pagar = models.ForeignKey(CuentaPorPagar, db_column='Cuenta_por_pagar_idCuenta_por_pagar')  # Field name made lowercase.
    fecha_pago_cuentaporpagar = models.DateTimeField(db_column='fecha_pago_cuentaPorPagar', default=timezone.now)  # Field name made lowercase.
    monto_pago_cuentaporpagar = models.DecimalField(db_column='monto_pago_cuentaPorPagar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey('TipoPago', db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.

    def __str__(self):
        return 'Id:%s - Cuenta: %s - Compra: %s - F: %s' % (self.idpago_cuenta_por_pagar, self.cuenta_por_pagar_idcuenta_por_pagar.idcuenta_por_pagar, self.cuenta_por_pagar_idcuenta_por_pagar.compra_idcompra.idcompra,self.fecha_pago_cuentaporpagar)

    class Meta:
        managed = True
        db_table = 'Pago_cuenta_por_pagar'


class PagosCuentaPorCobrar(models.Model):
    idpagos_cuenta_por_cobrar = models.AutoField(db_column='idPagos_cuenta_por_cobrar', primary_key=True)  # Field name made lowercase.
    cuenta_por_cobrar_idcuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, db_column='Cuenta_por_cobrar_idCuenta_por_cobrar')  # Field name made lowercase.
    fecha_pago_cuentaporcobrar = models.DateTimeField(db_column='fecha_pago_cuentaPorCobrar', default=timezone.now)  # Field name made lowercase.
    monto_pago_cuentaporcobrar = models.DecimalField(db_column='monto_pago_cuentaPorCobrar', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey('TipoPago', db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.

    def __str__(self):
        return 'Id:%s - %s - F: %s' % (self.idpagos_cuenta_por_cobrar, self.cuenta_por_cobrar_idcuenta_por_cobrar,self.fecha_pago_cuentaporcobrar)

    class Meta:
        managed = True
        db_table = 'Pagos_cuenta_por_cobrar'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombres_persona = models.CharField(max_length=100, blank=True, null=True)
    apellidos_persona = models.CharField(max_length=100, blank=True, null=True)
    telefonos_persona = models.CharField(max_length=36, blank=True, null=True)
    direccion_persona = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento_persona = models.DateField(blank=True, null=True)
    dpi_persona = models.CharField(max_length=13, blank=True, null=True)
    estado_persona = models.BooleanField(default=True)
    correoelectronico_persona = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return '%s - %s %s' % (self.idpersona, self.nombres_persona,self.apellidos_persona)

    class Meta:
        managed = True
        ordering=["nombres_persona","apellidos_persona"]
        db_table = 'Persona'


class Precio(models.Model):
    idprecio = models.AutoField(db_column='idPrecio', primary_key=True)  # Field name made lowercase.
    nombre_precio = models.CharField(max_length=45, blank=True, null=True)
    valor_precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fechainicial_precio = models.DateTimeField(db_column='fechaInicial_precio', blank=True, null=True, default=timezone.now)  # Field name made lowercase.
    estado_precio = models.BooleanField(default=True)
    fechafinal_precio = models.DateTimeField(db_column='fechaFinal_precio', blank=True, null=True)  # Field name made lowercase.
    producto_codigo_producto = models.ForeignKey('Producto', db_column='Producto_codigo_producto')  # Field name made lowercase.


    def __str__(self):
        return 'Prod: %s - Pre: %s - Fi: %s' % (self.producto_codigo_producto, self.valor_precio,self.fechainicial_precio)

    class Meta:
        managed = True
        db_table = 'Precio'


class Producto(models.Model):
    codigo_producto = models.AutoField(primary_key=True)
    descripcion_producto = models.TextField(max_length=250, blank=True, null=True)
    estado_producto = models.BooleanField(default=True)
    talla_idtalla = models.ForeignKey('Talla', db_column='Talla_idTalla')  # Field name made lowercase.
    genero_idgener = models.ForeignKey(Genero, db_column='Genero_idGener')  # Field name made lowercase.
    color_idcolor = models.ForeignKey(Color, db_column='Color_idColor')  # Field name made lowercase.
    tipo_producto_idtipo_producto = models.ForeignKey('TipoProducto', db_column='Tipo_producto_idTipo_producto')  # Field name made lowercase.
    codigobarras_producto = models.CharField(max_length=45, blank=True, null=True)
    codigoestilo_producto = models.CharField(max_length=45, blank=True, null=True)
    estilo_idestilo = models.ForeignKey(Estilo, db_column='Estilo_idEstilo')  # Field name made lowercase.
    nombre_producto = models.CharField(max_length=60, blank=True, null=True)
    marca_id_marca = models.ForeignKey(Marca, db_column='marca_idmarca')  # Field name made lowercase.
    publicar_producto = models.BooleanField(default=False)
    oferta_producto = models.BooleanField(default=False)
    #combo_idcombo = models.ForeignKey(Combo, db_column='Combo_idCombo')  # Field name made lowercase.
    def __str__(self):
        return '%s||%s||%s' % (self.codigo_producto,self.codigoestilo_producto,self.nombre_producto)

    class Meta:
        managed = True
        db_table = 'Producto'


class ProductoHasFotografia(models.Model):
    producto_codigo_producto = models.ForeignKey(Producto, db_column='Producto_codigo_producto')  # Field name made lowercase.
    fotografia_idfotografia = models.ForeignKey(Fotografia, db_column='Fotografia_idFotografia')  # Field name made lowercase.
    idproductohasfotografia = models.AutoField(db_column='idproductohasfotografia', primary_key=True)

    def __str__(self):
        return '%s --- %s' % (self.producto_codigo_producto,self.fotografia_idfotografia)

    class Meta:
        managed = True
        db_table = 'Producto_has_Fotografia'


class Promocion(models.Model):
    idpromocion = models.AutoField(db_column='idPromocion', primary_key=True)  # Field name made lowercase.
    nombre_promocion = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicialpromocion = models.DateField(db_column='fecha_inicialPromocion', blank=True, null=True, default=timezone.now)  # Field name made lowercase.
    fecha_finalpromocion = models.DateField(db_column='fecha_finalPromocion', blank=True, null=True)  # Field name made lowercase.
    valor_promocion = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado_promocion = models.BooleanField(default=True)

    def __str__(self):
        return '%s|%s|Fi:%s|%s' % (self.nombre_promocion,self.valor_promocion,self.fecha_inicialpromocion,self.idpromocion)

    class Meta:
        managed = True
        db_table = 'Promocion'


class PromocionHasProducto(models.Model):
    promocion_idpromocion = models.ForeignKey(Promocion, db_column='Promocion_idPromocion')  # Field name made lowercase.
    inventario_producto_idinventario_producto = models.ForeignKey(InventarioProducto, db_column='Inventario_producto_idInventario_producto')  # Field name made lowercase.
    idpromocionhasproducto = models.AutoField(db_column='idpromocionhasproducto', primary_key=True)
    #estado_promocion = models.BooleanField(default=True)
    cantidad_productoenpromocion=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s - Lote: %s - Prod: %s' % (self.promocion_idpromocion, self.inventario_producto_idinventario_producto.idinventario_producto,self.inventario_producto_idinventario_producto.producto_codigo_producto)

    class Meta:
        managed = True
        db_table = 'Promocion_has_Producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombre_proveedor = models.CharField(max_length=60, blank=True, null=True)
    direccion_proveedor = models.CharField(max_length=200, blank=True, null=True)
    telefonos_proveedor = models.CharField(max_length=36, blank=True, null=True)
    estado_proveedor = models.BooleanField(default=True)
    nit_proveedor = models.CharField(max_length=15, blank=True, null=True)
    casa_matrizproveedor = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.idproveedor,self.nombre_proveedor)

    class Meta:
        managed = True
        db_table = 'Proveedor'


class Puesto(models.Model):
    idpuesto = models.AutoField(db_column='idPuesto', primary_key=True)  # Field name made lowercase.
    nombre_puesto = models.CharField(max_length=50, blank=True, null=True)
    estado_puesto = models.BooleanField(default=True)
    #estandares_vendedor_idestandares_vendedor = models.ForeignKey('EstandaresVendedor', db_column='estandares_vendedor_idestandares_vendedor',null=True,blank=True)  # Field name made lowercase.
    ventasminimas_vendedor=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        ventas=""
        if not self.ventasminimas_vendedor:
            ventas=" "
        else:
            ventas="-"+str(self.ventasminimas_vendedor)
        return '%s-%s%s' % (self.idpuesto,self.nombre_puesto,ventas)

    class Meta:
        managed = True
        db_table = 'Puesto'


class Seguridad(models.Model):
    idseguridad = models.AutoField(db_column='idSeguridad', primary_key=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, db_column='Cliente_idCliente')  # Field name made lowercase.
    pregunta_seguridad = models.CharField(max_length=60, blank=True, null=True)
    respuesta_seguridad = models.CharField(max_length=60, blank=True, null=True)
    estado_seguridad = models.BooleanField(default=True)

    def __str__(self):
        return '%s - Cli: %s' % (self.idseguridad,self.cliente_idcliente)

    class Meta:
        managed = True
        db_table = 'Seguridad'


class Sucursal(models.Model):
    idsucursal = models.AutoField(db_column='idSucursal', primary_key=True)  # Field name made lowercase.
    nombre_sucursal = models.CharField(max_length=60, blank=True, null=True)
    direccion_sucursal = models.CharField(max_length=200, blank=True, null=True)
    telefonos_sucursal = models.CharField(max_length=36, blank=True, null=True)
    estado_sucursal = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.idsucursal,self.nombre_sucursal)

    class Meta:
        managed = True
        db_table = 'Sucursal'


class Talla(models.Model):
    idtalla = models.AutoField(db_column='idTalla', primary_key=True)  # Field name made lowercase.
    nombre_talla = models.CharField(db_column='nombre_Talla', max_length=10)  # Field name made lowercase.
    estado_talla = models.BooleanField(default=True)  # This field type is a guess.

    def __str__(self):
        return '%s' % (self.nombre_talla)

    class Meta:
        managed = True
        ordering=["nombre_talla"]
        db_table = 'Talla'


class TipoCliente(models.Model):
    idtipo_cliente = models.AutoField(db_column='idTipo_cliente', primary_key=True)  # Field name made lowercase.
    nombre_tipocliente = models.CharField(db_column='nombre_tipoCliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    estado_tipocliente = models.BooleanField(db_column='estado_tipoCliente', default=True)  # Field name made lowercase.
    #estandarcliente_idestandarcliente = models.ForeignKey('EstandarCliente', db_column='estandarcliente_idestandarcliente',blank=True,null=True)  # Field name made lowercase.
    comprasminimas_cliente=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.idtipo_cliente,self.nombre_tipocliente)

    class Meta:
        managed = True
        db_table = 'Tipo_cliente'


class TipoPago(models.Model):
    idtipo_pago = models.AutoField(db_column='idTipo_pago', primary_key=True)  # Field name made lowercase.
    nombre_tipopago = models.CharField(db_column='nombre_tipoPago', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado_tipopago = models.BooleanField(db_column='estado_tipoPago', default=True)  # Field name made lowercase.

    def __str__(self):
        return '%s - %s' % (self.idtipo_pago,self.nombre_tipopago)

    class Meta:
        managed = True
        db_table = 'Tipo_pago'


class TipoProducto(models.Model):
    idtipo_producto = models.AutoField(db_column='idTipo_producto', primary_key=True)  # Field name made lowercase.
    nombre_tipoproducto = models.CharField(db_column='nombre_tipoProducto', max_length=50)  # Field name made lowercase.
    #marca_id_marca = models.ForeignKey(Marca, db_column='Marca_id_marca')  # Field name made lowercase.
    estado_tipoproducto = models.BooleanField(db_column='estado_tipoProducto', default=True)  # Field name made lowercase.

    def __str__(self):
        return '%s' % (self.nombre_tipoproducto)

    class Meta:
        managed = True
        ordering=["nombre_tipoproducto"]
        db_table = 'Tipo_producto'


class TrasladoMercaderia(models.Model):
    idtraslado_mercaderia = models.AutoField(db_column='idTraslado_mercaderia', primary_key=True)  # Field name made lowercase.
    bodega_egreso = models.ForeignKey(Bodega, db_column='Bodega_egreso',related_name='bodega_bodega_egreso')  # Field name made lowercase.
    bodega_ingreso = models.ForeignKey(Bodega, db_column='Bodega_ingreso',related_name='bodega_bodega_ingreso')  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado')  # Field name made lowercase.
    motivo_idmotivo = models.ForeignKey(Motivo, db_column='Motivo_idMotivo')  # Field name made lowercase.
    fecha_trasladomercaderia = models.DateTimeField(db_column='fecha_trasladoMercaderia', default=timezone.now)  # Field name made lowercase.

    def __str__(self):
        return '%s - O:%s D: %s F: %s' % (self.idtraslado_mercaderia,self.bodega_egreso,self.bodega_ingreso,self.fecha_trasladomercaderia)

    class Meta:
        managed = True
        db_table = 'Traslado_mercaderia'



class Venta(models.Model):
    idventa = models.AutoField(db_column='idVenta', primary_key=True)  # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, db_column='Empleado_idEmpleado',blank=True,null=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, db_column='Cliente_idCliente')  # Field name made lowercase.
    caja_idcaja = models.ForeignKey(Caja, db_column='Caja_idCaja')  # Field name made lowercase.
    tipo_pago_idtipo_pago = models.ForeignKey(TipoPago, db_column='Tipo_pago_idTipo_pago')  # Field name made lowercase.
    fecha_venta = models.DateTimeField(default=timezone.now)#models.DateTimeField(default=timezone.now)
    total_venta = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    contado_venta = models.BooleanField(default=True)
    estado_venta = models.BooleanField(default=True)
    anotaciones_venta = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    vendedor_venta = models.ForeignKey('Empleado', db_column='vendedor_venta',related_name='empleado_empleado_vendio')  # Field name made lowercase.
    es_cotizacion = models.BooleanField(default=False)

    def __str__(self):
        return '%s - Cli: %s F: %s' % (self.idventa,self.cliente_idcliente,self.fecha_venta)

    class Meta:
        managed = True
        db_table = 'Venta'
