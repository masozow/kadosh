# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AjusteInventario',
            fields=[
                ('idajuste_inventario', models.AutoField(db_column='idAjuste_inventario', serialize=False, primary_key=True)),
                ('fecha_horaajuste', models.DateTimeField(db_column='fecha_horaAjuste', default=django.utils.timezone.now)),
            ],
            options={
                'managed': True,
                'db_table': 'Ajuste_inventario',
            },
        ),
        migrations.CreateModel(
            name='Anaquel',
            fields=[
                ('idanaquel', models.AutoField(db_column='idAnaquel', serialize=False, primary_key=True)),
                ('codigo_anaquel', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_anaquel', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Anaquel',
            },
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('idbodega', models.AutoField(db_column='idBodega', serialize=False, primary_key=True)),
                ('nombre_bodega', models.CharField(null=True, max_length=45, blank=True)),
                ('descripcion_bodega', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_bodega', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Bodega',
            },
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('idcaja', models.AutoField(db_column='idCaja', serialize=False, primary_key=True)),
                ('descripcion_caja', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_caja', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Caja',
            },
        ),
        migrations.CreateModel(
            name='CajaHasEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('momento_asignacion_caja', models.DateTimeField(default=django.utils.timezone.now)),
                ('momento_desasignacion_caja', models.DateTimeField(null=True, blank=True)),
                ('caja_idcaja', models.ForeignKey(db_column='Caja_idCaja', to='kadoshapp.Caja')),
            ],
            options={
                'managed': True,
                'db_table': 'Caja_has_Empleado',
            },
        ),
        migrations.CreateModel(
            name='CierreDeCaja',
            fields=[
                ('idcierre_de_caja', models.AutoField(db_column='idCierre_de_caja', serialize=False, primary_key=True)),
                ('fecha_cierredecaja', models.DateField(db_column='fecha_cierreDeCaja', default=django.utils.timezone.now)),
                ('total_real_cierredecaja', models.DecimalField(null=True, decimal_places=2, db_column='total_real_cierreDeCaja', max_digits=12, blank=True)),
                ('total_calculado_cierredecaja', models.DecimalField(null=True, decimal_places=2, db_column='total_calculado_cierreDeCaja', max_digits=12, blank=True)),
                ('finalizado_cierredecaja', models.BooleanField(db_column='finalizado_cierreDeCaja', default=True)),
                ('caja_idcaja', models.ForeignKey(db_column='Caja_idCaja', to='kadoshapp.Caja')),
            ],
            options={
                'managed': True,
                'db_table': 'Cierre_de_caja',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idcliente', models.AutoField(db_column='idCliente', serialize=False, primary_key=True)),
                ('nit_cliente', models.CharField(null=True, max_length=13, blank=True)),
                ('estado_cliente', models.BooleanField(default=True)),
                ('fecha_registro_cliente', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'managed': True,
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('idcolor', models.AutoField(db_column='idColor', serialize=False, primary_key=True)),
                ('nombre_color', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_color', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Color',
            },
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('idcombo', models.AutoField(db_column='idCombo', serialize=False, primary_key=True)),
                ('nombre_combo', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_combo', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Combo',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idcompra', models.AutoField(db_column='idCompra', serialize=False, primary_key=True)),
                ('estado_compra', models.BooleanField(default=True)),
                ('fecha_compra', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_compra', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
                ('entregada_compra', models.BooleanField(default=True)),
                ('contado_compra', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Compra',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idcontacto', models.AutoField(db_column='idContacto', serialize=False, primary_key=True)),
                ('correo_contacto', models.CharField(null=True, max_length=45, blank=True)),
                ('nombre_contacto', models.CharField(null=True, max_length=50, blank=True)),
                ('asunto_contacto', models.CharField(null=True, max_length=60, blank=True)),
                ('mensaje_contacto', models.CharField(null=True, max_length=400, blank=True)),
                ('estado_contacto', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Contacto',
            },
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('idcontenido', models.AutoField(db_column='idContenido', serialize=False, primary_key=True)),
                ('resumen_contenido', models.CharField(null=True, max_length=45, blank=True)),
                ('texto_contenido', models.CharField(null=True, max_length=100, blank=True)),
                ('estado_contenido', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Contenido',
            },
        ),
        migrations.CreateModel(
            name='CuentaPorCobrar',
            fields=[
                ('idcuenta_por_cobrar', models.AutoField(db_column='idCuenta_por_cobrar', serialize=False, primary_key=True)),
                ('saldo_inicial_cuentaporcobrar', models.DecimalField(null=True, decimal_places=2, db_column='saldo_inicial_cuentaPorCobrar', max_digits=12, blank=True)),
                ('saldo_actual_cuentaporcobrar', models.DecimalField(null=True, decimal_places=2, db_column='saldo_actual_cuentaPorCobrar', max_digits=12, blank=True)),
                ('fecha_pagofinal_cuentaporcobrar', models.DateField(null=True, db_column='fecha_pagoFinal_cuentaPorCobrar', blank=True)),
                ('estado_cuentaporcobrar', models.BooleanField(db_column='estado_cuentaPorCobrar', default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Cuenta_por_cobrar',
            },
        ),
        migrations.CreateModel(
            name='CuentaPorPagar',
            fields=[
                ('idcuenta_por_pagar', models.AutoField(db_column='idCuenta_por_pagar', serialize=False, primary_key=True)),
                ('saldo_inicial_cuentaporpagar', models.DecimalField(null=True, decimal_places=2, db_column='saldo_inicial_cuentaPorPagar', max_digits=12, blank=True)),
                ('saldo_actual_cuentaporpagar', models.DecimalField(null=True, decimal_places=2, db_column='saldo_actual_cuentaPorPagar', max_digits=12, blank=True)),
                ('fecha_pagofinal_cuentaporpagar', models.DateField(null=True, db_column='fecha_pagofinal_cuentaPorPagar', blank=True)),
                ('estado_cuentaporpagar', models.BooleanField(db_column='estado_cuentaPorPagar', default=True)),
                ('compra_idcompra', models.ForeignKey(db_column='Compra_idCompra', to='kadoshapp.Compra')),
            ],
            options={
                'managed': True,
                'db_table': 'Cuenta_por_pagar',
            },
        ),
        migrations.CreateModel(
            name='DatosEnvio',
            fields=[
                ('iddatos_envio', models.AutoField(db_column='idDatos_envio', serialize=False, primary_key=True)),
                ('nombres_envio', models.CharField(null=True, max_length=80, blank=True)),
                ('apellidos_envio', models.CharField(null=True, max_length=80, blank=True)),
                ('correo_electronico_envio', models.CharField(null=True, max_length=60, blank=True)),
                ('telefonos_envio', models.CharField(null=True, max_length=36, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Datos_envio',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('cantidad_compra', models.IntegerField(null=True, blank=True)),
                ('valor_parcial_compra', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
                ('iddetallecompra', models.AutoField(db_column='idDetalleCompra', serialize=False, primary_key=True)),
                ('compra_idcompra', models.ForeignKey(db_column='Compra_idCompra', to='kadoshapp.Compra')),
            ],
            options={
                'managed': True,
                'db_table': 'Detalle_compra',
            },
        ),
        migrations.CreateModel(
            name='DetalleInventarioRealizado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cantidad_real_inventario_realizado', models.IntegerField(null=True, blank=True)),
                ('ajuste_inventario_idajuste_inventario', models.ForeignKey(db_column='Ajuste_inventario_idAjuste_inventario', to='kadoshapp.AjusteInventario')),
            ],
            options={
                'managed': True,
                'db_table': 'Detalle inventario_realizado',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('iddetalleventa', models.AutoField(db_column='idDetalleVenta', serialize=False, primary_key=True)),
                ('cantidad_venta', models.IntegerField(null=True, blank=True)),
                ('valor_parcial_venta', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Detalle_venta',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idempleado', models.AutoField(db_column='idEmpleado', serialize=False, primary_key=True)),
                ('fecha_contratacion_empleado', models.DateField(default=django.utils.timezone.now)),
                ('codigo_autorización_empleado', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_empleado', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('idenvio', models.AutoField(db_column='idEnvio', serialize=False, primary_key=True)),
                ('repartidor_envio', models.CharField(null=True, max_length=50, blank=True)),
                ('salida_envio', models.BooleanField(default=False)),
                ('encamino_envio', models.BooleanField(db_column='enCamino_envio', default=False)),
                ('entregado_envio', models.BooleanField(default=False)),
                ('momentosolicitud_envio', models.DateTimeField(db_column='momentoSolicitud_envio', default=django.utils.timezone.now)),
                ('estado_envio', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Envio',
            },
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('idestilo', models.AutoField(db_column='idEstilo', serialize=False, primary_key=True)),
                ('nombre_estilo', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_estilo', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Estilo',
            },
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('idfotografia', models.AutoField(db_column='idFotografia', serialize=False, primary_key=True)),
                ('nombre_fotografia', models.CharField(null=True, max_length=45, blank=True)),
                ('ruta_fotografia', models.ImageField(upload_to='/fotografias')),
                ('estado_fotografia', models.BooleanField(default=True)),
                ('principal_fotografia', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
                'db_table': 'Fotografia',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgener', models.AutoField(db_column='idGener', serialize=False, primary_key=True)),
                ('nombre_genero', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_genero', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('idindex', models.AutoField(db_column='idIndex', serialize=False, primary_key=True)),
                ('titulo_index', models.CharField(null=True, max_length=60, blank=True)),
                ('parrafo_index', models.CharField(null=True, max_length=400, blank=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Index',
            },
        ),
        migrations.CreateModel(
            name='IndexHasFotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('ubicacion_fotografiaindex', models.SmallIntegerField(null=True, db_column='ubicacion_fotografiaIndex', blank=True)),
                ('fotografia_idfotografia', models.ForeignKey(db_column='Fotografia_idFotografia', to='kadoshapp.Fotografia')),
                ('index_idindex', models.ForeignKey(db_column='Index_idIndex', to='kadoshapp.Index')),
            ],
            options={
                'managed': True,
                'db_table': 'Index_has_Fotografia',
            },
        ),
        migrations.CreateModel(
            name='InventarioProducto',
            fields=[
                ('idinventario_producto', models.AutoField(db_column='idInventario_producto', serialize=False, primary_key=True)),
                ('existencia_minima', models.IntegerField(null=True, blank=True)),
                ('existencia_maxima', models.IntegerField(null=True, blank=True)),
                ('existencia_actual', models.IntegerField(null=True, blank=True)),
                ('fecha_creacioninventario', models.DateTimeField(db_column='fecha_creacionInventario', default=django.utils.timezone.now)),
                ('estado_inventario_producto', models.BooleanField(default=True)),
                ('anaquel_idanaquel', models.ForeignKey(db_column='Anaquel_idAnaquel', to='kadoshapp.Anaquel')),
            ],
            options={
                'managed': True,
                'db_table': 'Inventario_producto',
            },
        ),
        migrations.CreateModel(
            name='InventarioRealizado',
            fields=[
                ('idinventario_realizado', models.AutoField(db_column='idInventario_realizado', serialize=False, primary_key=True)),
                ('fecha_realizacion_inventario', models.DateTimeField(default=django.utils.timezone.now)),
                ('completo_inventario', models.BooleanField()),
                ('estado_inventario', models.BooleanField(default=True)),
                ('empleado_idempleado', models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado')),
            ],
            options={
                'managed': True,
                'db_table': 'Inventario_realizado',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_marca', models.CharField(null=True, max_length=50, blank=True)),
                ('estado_marca', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('idmotivo', models.AutoField(db_column='idMotivo', serialize=False, primary_key=True)),
                ('nombre_motivo', models.CharField(null=True, max_length=45, blank=True)),
                ('estado_motivo', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Motivo',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('idnoticia', models.AutoField(db_column='idNoticia', serialize=False, primary_key=True)),
                ('momento_publicacion_noticia', models.DateTimeField(default=django.utils.timezone.now)),
                ('titulo_noticia', models.CharField(null=True, max_length=70, blank=True)),
                ('contenido_noticia', models.CharField(null=True, max_length=600, blank=True)),
                ('estado_noticia', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Noticia',
            },
        ),
        migrations.CreateModel(
            name='NoticiaHasFotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('vista_previa', models.BooleanField(default=True)),
                ('fotografia_idfotografia', models.ForeignKey(db_column='Fotografia_idFotografia', to='kadoshapp.Fotografia')),
                ('noticia_idnoticia', models.ForeignKey(db_column='Noticia_idNoticia', to='kadoshapp.Noticia')),
            ],
            options={
                'managed': True,
                'db_table': 'Noticia_has_Fotografia',
            },
        ),
        migrations.CreateModel(
            name='PagoCuentaPorPagar',
            fields=[
                ('idpago_cuenta_por_pagar', models.AutoField(db_column='idPago_cuenta_por_pagar', serialize=False, primary_key=True)),
                ('fecha_pago_cuentaporpagar', models.DateTimeField(db_column='fecha_pago_cuentaPorPagar', default=django.utils.timezone.now)),
                ('monto_pago_cuentaporpagar', models.DecimalField(null=True, decimal_places=2, db_column='monto_pago_cuentaPorPagar', max_digits=12, blank=True)),
                ('cuenta_por_pagar_idcuenta_por_pagar', models.ForeignKey(db_column='Cuenta_por_pagar_idCuenta_por_pagar', to='kadoshapp.CuentaPorPagar')),
            ],
            options={
                'managed': True,
                'db_table': 'Pago_cuenta_por_pagar',
            },
        ),
        migrations.CreateModel(
            name='PagosCuentaPorCobrar',
            fields=[
                ('idpagos_cuenta_por_cobrar', models.AutoField(db_column='idPagos_cuenta_por_cobrar', serialize=False, primary_key=True)),
                ('fecha_pago_cuentaporcobrar', models.DateTimeField(db_column='fecha_pago_cuentaPorCobrar', default=django.utils.timezone.now)),
                ('monto_pago_cuentaporcobrar', models.DecimalField(null=True, decimal_places=2, db_column='monto_pago_cuentaPorCobrar', max_digits=12, blank=True)),
                ('cuenta_por_cobrar_idcuenta_por_cobrar', models.ForeignKey(db_column='Cuenta_por_cobrar_idCuenta_por_cobrar', to='kadoshapp.CuentaPorCobrar')),
            ],
            options={
                'managed': True,
                'db_table': 'Pagos_cuenta_por_cobrar',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.AutoField(db_column='idPersona', serialize=False, primary_key=True)),
                ('nombres_persona', models.CharField(null=True, max_length=100, blank=True)),
                ('apellidos_persona', models.CharField(null=True, max_length=100, blank=True)),
                ('telefonos_persona', models.CharField(null=True, max_length=36, blank=True)),
                ('direccion_persona', models.CharField(null=True, max_length=200, blank=True)),
                ('fecha_nacimiento_persona', models.DateField(null=True, blank=True)),
                ('dpi_persona', models.CharField(null=True, max_length=13, blank=True)),
                ('estado_persona', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('idprecio', models.AutoField(db_column='idPrecio', serialize=False, primary_key=True)),
                ('nombre_precio', models.CharField(null=True, max_length=45, blank=True)),
                ('valor_precio', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
                ('fechainicial_precio', models.DateTimeField(null=True, db_column='fechaInicial_precio', blank=True)),
                ('fechafinal_precio', models.DateTimeField(null=True, db_column='fechaFinal_precio', blank=True)),
                ('estado_precio', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Precio',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.CharField(max_length=25, serialize=False, primary_key=True)),
                ('descripcion_producto', models.CharField(null=True, max_length=250, blank=True)),
                ('estado_producto', models.BooleanField(default=True)),
                ('color_idcolor', models.ForeignKey(db_column='Color_idColor', to='kadoshapp.Color')),
                ('combo_idcombo', models.ForeignKey(db_column='Combo_idCombo', to='kadoshapp.Combo')),
                ('estilo_idestilo', models.ForeignKey(db_column='Estilo_idEstilo', to='kadoshapp.Estilo')),
                ('genero_idgener', models.ForeignKey(db_column='Genero_idGener', to='kadoshapp.Genero')),
            ],
            options={
                'managed': True,
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='ProductoHasFotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fotografia_idfotografia', models.ForeignKey(db_column='Fotografia_idFotografia', to='kadoshapp.Fotografia')),
                ('producto_codigo_producto', models.ForeignKey(db_column='Producto_codigo_producto', to='kadoshapp.Producto')),
            ],
            options={
                'managed': True,
                'db_table': 'Producto_has_Fotografia',
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('idpromocion', models.AutoField(db_column='idPromocion', serialize=False, primary_key=True)),
                ('nombre_promocion', models.CharField(null=True, max_length=50, blank=True)),
                ('fecha_inicialpromocion', models.DateField(null=True, db_column='fecha_inicialPromocion', blank=True)),
                ('fecha_finalpromocion', models.DateField(null=True, db_column='fecha_finalPromocion', blank=True)),
                ('valor_promocion', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
                ('estado_promocion', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Promocion',
            },
        ),
        migrations.CreateModel(
            name='PromocionHasProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('inventario_producto_idinventario_producto', models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto')),
                ('promocion_idpromocion', models.ForeignKey(db_column='Promocion_idPromocion', to='kadoshapp.Promocion')),
            ],
            options={
                'managed': True,
                'db_table': 'Promocion_has_Producto',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idproveedor', models.AutoField(db_column='idProveedor', serialize=False, primary_key=True)),
                ('nombre_proveedor', models.CharField(null=True, max_length=60, blank=True)),
                ('direccion_proveedor', models.CharField(null=True, max_length=200, blank=True)),
                ('telefonos_proveedor', models.CharField(null=True, max_length=36, blank=True)),
                ('estado_proveedor', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('idpuesto', models.AutoField(db_column='idPuesto', serialize=False, primary_key=True)),
                ('nombre_puesto', models.CharField(null=True, max_length=50, blank=True)),
                ('estado_puesto', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Puesto',
            },
        ),
        migrations.CreateModel(
            name='Seguridad',
            fields=[
                ('idseguridad', models.AutoField(db_column='idSeguridad', serialize=False, primary_key=True)),
                ('pregunta_seguridad', models.CharField(null=True, max_length=60, blank=True)),
                ('respuesta_seguridad', models.CharField(null=True, max_length=60, blank=True)),
                ('estado_seguridad', models.BooleanField(default=True)),
                ('cliente_idcliente', models.ForeignKey(db_column='Cliente_idCliente', to='kadoshapp.Cliente')),
            ],
            options={
                'managed': True,
                'db_table': 'Seguridad',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idsucursal', models.AutoField(db_column='idSucursal', serialize=False, primary_key=True)),
                ('nombre_sucursal', models.CharField(null=True, max_length=60, blank=True)),
                ('direccion_sucursal', models.CharField(null=True, max_length=200, blank=True)),
                ('telefonos_sucursal', models.CharField(null=True, max_length=36, blank=True)),
                ('estado_sucursal', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Sucursal',
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('idtalla', models.IntegerField(db_column='idTalla', serialize=False, primary_key=True)),
                ('nombre_talla', models.CharField(null=True, max_length=5, db_column='nombre_Talla', blank=True)),
                ('estado_talla', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Talla',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('idtipo_cliente', models.AutoField(db_column='idTipo_cliente', serialize=False, primary_key=True)),
                ('nombre_tipocliente', models.CharField(null=True, max_length=45, db_column='nombre_tipoCliente', blank=True)),
                ('estado_tipocliente', models.BooleanField(db_column='estado_tipoCliente', default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Tipo_cliente',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('idtipo_pago', models.AutoField(db_column='idTipo_pago', serialize=False, primary_key=True)),
                ('nombre_tipopago', models.CharField(null=True, max_length=50, db_column='nombre_tipoPago', blank=True)),
                ('estado_tipopago', models.BooleanField(db_column='estado_tipoPago', default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Tipo_pago',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('idtipo_producto', models.AutoField(db_column='idTipo_producto', serialize=False, primary_key=True)),
                ('nombre_tipoproducto', models.CharField(null=True, max_length=50, db_column='nombre_tipoProducto', blank=True)),
                ('estado_tipoproducto', models.BooleanField(db_column='estado_tipoProducto', default=True)),
                ('marca_id_marca', models.ForeignKey(db_column='Marca_id_marca', to='kadoshapp.Marca')),
            ],
            options={
                'managed': True,
                'db_table': 'Tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='TrasladoMercaderia',
            fields=[
                ('idtraslado_mercaderia', models.AutoField(db_column='idTraslado_mercaderia', serialize=False, primary_key=True)),
                ('fecha_trasladomercaderia', models.DateTimeField(db_column='fecha_trasladoMercaderia', default=django.utils.timezone.now)),
                ('bodega_egreso', models.ForeignKey(db_column='Bodega_egreso', to='kadoshapp.Bodega', related_name='bodega_bodega_egreso')),
                ('bodega_ingreso', models.ForeignKey(db_column='Bodega_ingreso', to='kadoshapp.Bodega', related_name='bodega_bodega_ingreso')),
                ('empleado_idempleado', models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado')),
                ('motivo_idmotivo', models.ForeignKey(db_column='Motivo_idMotivo', to='kadoshapp.Motivo')),
            ],
            options={
                'managed': True,
                'db_table': 'Traslado_mercaderia',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.AutoField(db_column='idVenta', serialize=False, primary_key=True)),
                ('fecha_venta', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_venta', models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True)),
                ('contado_venta', models.BooleanField(default=True)),
                ('estado_venta', models.BooleanField(default=True)),
                ('caja_idcaja', models.ForeignKey(db_column='Caja_idCaja', to='kadoshapp.Caja')),
                ('cliente_idcliente', models.ForeignKey(db_column='Cliente_idCliente', to='kadoshapp.Cliente')),
                ('empleado_idempleado', models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado')),
                ('tipo_pago_idtipo_pago', models.ForeignKey(db_column='Tipo_pago_idTipo_pago', to='kadoshapp.TipoPago')),
            ],
            options={
                'managed': True,
                'db_table': 'Venta',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='talla_idtalla',
            field=models.ForeignKey(db_column='Talla_idTalla', to='kadoshapp.Talla'),
        ),
        migrations.AddField(
            model_name='precio',
            name='producto_codigo_producto',
            field=models.ForeignKey(db_column='Producto_codigo_producto', to='kadoshapp.Producto'),
        ),
        migrations.AddField(
            model_name='pagoscuentaporcobrar',
            name='tipo_pago_idtipo_pago',
            field=models.ForeignKey(db_column='Tipo_pago_idTipo_pago', to='kadoshapp.TipoPago'),
        ),
        migrations.AddField(
            model_name='inventarioproducto',
            name='producto_codigo_producto',
            field=models.ForeignKey(db_column='Producto_codigo_producto', to='kadoshapp.Producto'),
        ),
        migrations.AddField(
            model_name='estilo',
            name='tipo_producto_idtipo_producto',
            field=models.ForeignKey(db_column='Tipo_producto_idTipo_producto', to='kadoshapp.TipoProducto'),
        ),
        migrations.AddField(
            model_name='envio',
            name='venta_idventa',
            field=models.ForeignKey(db_column='Venta_idVenta', to='kadoshapp.Venta'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='persona_idpersona',
            field=models.ForeignKey(db_column='Persona_idPersona', to='kadoshapp.Persona'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto_idpuesto',
            field=models.ForeignKey(db_column='Puesto_idPuesto', to='kadoshapp.Puesto'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal_idsucursal',
            field=models.ForeignKey(db_column='Sucursal_idSucursal', to='kadoshapp.Sucursal'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta_idventa',
            field=models.ForeignKey(db_column='Venta_idVenta', to='kadoshapp.Venta'),
        ),
        migrations.AddField(
            model_name='detalleinventariorealizado',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto'),
        ),
        migrations.AddField(
            model_name='detalleinventariorealizado',
            name='inventario_realizado_idinventario_realizado',
            field=models.ForeignKey(db_column='Inventario_realizado_idInventario_realizado', to='kadoshapp.InventarioRealizado'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto'),
        ),
        migrations.AddField(
            model_name='datosenvio',
            name='envio_idenvio',
            field=models.ForeignKey(db_column='Envio_idEnvio', to='kadoshapp.Envio'),
        ),
        migrations.AddField(
            model_name='cuentaporcobrar',
            name='venta_idventa',
            field=models.ForeignKey(db_column='Venta_idVenta', to='kadoshapp.Venta'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='index_idindex',
            field=models.ForeignKey(db_column='Index_idIndex', to='kadoshapp.Index'),
        ),
        migrations.AddField(
            model_name='compra',
            name='empleado_idempleado',
            field=models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado'),
        ),
        migrations.AddField(
            model_name='compra',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor_idproveedor',
            field=models.ForeignKey(db_column='Proveedor_idProveedor', to='kadoshapp.Proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_pago_idtipo_pago',
            field=models.ForeignKey(db_column='Tipo_pago_idTipo_pago', to='kadoshapp.TipoPago'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='persona_idpersona',
            field=models.ForeignKey(db_column='Persona_idPersona', to='kadoshapp.Persona'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente_idtipo_cliente',
            field=models.ForeignKey(db_column='Tipo_cliente_idTipo_cliente', to='kadoshapp.TipoCliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cierredecaja',
            name='empleado_idempleado',
            field=models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado'),
        ),
        migrations.AddField(
            model_name='cajahasempleado',
            name='empleado_idempleado',
            field=models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado'),
        ),
        migrations.AddField(
            model_name='caja',
            name='sucursal_idsucursal',
            field=models.ForeignKey(db_column='Sucursal_idSucursal', to='kadoshapp.Sucursal'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='sucursal_idsucursal',
            field=models.ForeignKey(db_column='Sucursal_idSucursal', to='kadoshapp.Sucursal'),
        ),
        migrations.AddField(
            model_name='anaquel',
            name='bodega_idbodega',
            field=models.ForeignKey(db_column='Bodega_idBodega', to='kadoshapp.Bodega'),
        ),
        migrations.AddField(
            model_name='ajusteinventario',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(db_column='Inventario_producto_idInventario_producto', to='kadoshapp.InventarioProducto'),
        ),
        migrations.AddField(
            model_name='ajusteinventario',
            name='motivo_idmotivo',
            field=models.ForeignKey(db_column='Motivo_idMotivo', to='kadoshapp.Motivo'),
        ),
        migrations.AlterUniqueTogether(
            name='productohasfotografia',
            unique_together=set([('fotografia_idfotografia', 'producto_codigo_producto')]),
        ),
        migrations.AlterUniqueTogether(
            name='noticiahasfotografia',
            unique_together=set([('noticia_idnoticia', 'fotografia_idfotografia')]),
        ),
        migrations.AlterUniqueTogether(
            name='indexhasfotografia',
            unique_together=set([('index_idindex', 'fotografia_idfotografia')]),
        ),
    ]
