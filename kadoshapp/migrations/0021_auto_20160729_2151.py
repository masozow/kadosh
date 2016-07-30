# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kadoshapp', '0020_promocionhasproducto_cantidad_productoenpromocion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('iddescuento', models.AutoField(db_column='idDescuento', primary_key=True, serialize=False)),
                ('descripcion_descuento', models.CharField(blank=True, null=True, max_length=60)),
                ('monto_descuento', models.DecimalField(blank=True, db_column='monto_descuento', decimal_places=2, max_digits=12, null=True)),
                ('porcentaje_descuento', models.BooleanField(db_column='porcentaje_descuento', default=False)),
                ('estado_descuento', models.BooleanField(db_column='estado_descuento', default=True)),
                ('autorizado_descuento', models.BooleanField(db_column='autorizado_descuento', default=False)),
            ],
            options={
                'managed': True,
                'db_table': 'Descuento',
            },
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('iddevoucion', models.AutoField(db_column='idDevolucion', primary_key=True, serialize=False)),
                ('motivo_devolucion', models.CharField(blank=True, null=True, max_length=100)),
                ('momento_devolucion', models.DateTimeField(default=django.utils.timezone.now)),
                ('involucra_cambiodevolucion', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'db_table': 'Devolucion',
            },
        ),
        migrations.CreateModel(
            name='EstandarCliente',
            fields=[
                ('idestandarcliente', models.AutoField(db_column='idEstandarCliente', primary_key=True, serialize=False)),
                ('categoria_cliente', models.CharField(blank=True, null=True, max_length=45)),
                ('comprasminimas_cliente', models.DecimalField(blank=True, max_digits=12, decimal_places=2, null=True)),
                ('estado_estandarcliente', models.BooleanField(default=True)),
                ('tipo_cliente_idtipo_cliente', models.ForeignKey(db_column='Tipo_cliente_idTipo_cliente', to='kadoshapp.TipoCliente')),
            ],
            options={
                'managed': True,
                'db_table': 'EstandarCliente',
            },
        ),
        migrations.CreateModel(
            name='EstandaresVendedor',
            fields=[
                ('idestandares_vendedor', models.AutoField(db_column='idEstandares_vendedor', primary_key=True, serialize=False)),
                ('categoria_vendedor', models.CharField(blank=True, null=True, max_length=45)),
                ('ventasminimas_cliente', models.DecimalField(blank=True, max_digits=12, decimal_places=2, null=True)),
                ('estado_estandarvendedor', models.BooleanField(default=True)),
                ('puesto_idpuesto', models.ForeignKey(db_column='Puesto_idPuesto', to='kadoshapp.Puesto')),
            ],
            options={
                'managed': True,
                'db_table': 'EstandarCliente',
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('idgastos', models.AutoField(db_column='idGastos', primary_key=True, serialize=False)),
                ('monto_gasto', models.DecimalField(blank=True, max_digits=12, decimal_places=2, null=True)),
                ('motivo_gasto', models.CharField(blank=True, null=True, max_length=60)),
                ('momento_gasto', models.DateTimeField(default=django.utils.timezone.now)),
                ('caja_idcaja', models.ForeignKey(db_column='Caja_idCaja', to='kadoshapp.Caja')),
            ],
            options={
                'managed': True,
                'db_table': 'Gastos',
            },
        ),
        migrations.CreateModel(
            name='MarcaHasTipoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('marca_idmarca', models.ForeignKey(db_column='Marca_id_marca', to='kadoshapp.Marca')),
            ],
            options={
                'managed': True,
                'db_table': 'Marca_has_Tipo_producto',
            },
        ),
        migrations.RemoveField(
            model_name='detalleinventariorealizado',
            name='ajuste_inventario_idajuste_inventario',
        ),
        migrations.RemoveField(
            model_name='detalleinventariorealizado',
            name='inventario_producto_idinventario_producto',
        ),
        migrations.RemoveField(
            model_name='detalleinventariorealizado',
            name='inventario_realizado_idinventario_realizado',
        ),
        migrations.RemoveField(
            model_name='inventariorealizado',
            name='empleado_idempleado',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='inventario_producto_idinventario_producto',
        ),
        migrations.RemoveField(
            model_name='estilo',
            name='tipo_producto_idtipo_producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='combo_idcombo',
        ),
        migrations.RemoveField(
            model_name='promocionhasproducto',
            name='estado_promocion',
        ),
        migrations.RemoveField(
            model_name='tipoproducto',
            name='marca_id_marca',
        ),
        migrations.AddField(
            model_name='ajusteinventario',
            name='cantidad_real_ajuste',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ajusteinventario',
            name='empleado_idempleado',
            field=models.ForeignKey(to='kadoshapp.Empleado', default=1, db_column='Empleado_idEmpleado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cierredecaja',
            name='total_cheque_cierredecaja',
            field=models.DecimalField(blank=True, db_column='total_cheque_cierreDeCaja', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='cierredecaja',
            name='total_efectivo_cierredecaja',
            field=models.DecimalField(blank=True, db_column='total_efectivo_cierreDeCaja', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='cierredecaja',
            name='total_egresos_cierredecaja',
            field=models.DecimalField(blank=True, db_column='total_egresos_cierreDeCaja', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='cierredecaja',
            name='total_tarjeta_cierredecaja',
            field=models.DecimalField(blank=True, db_column='total_tarjeta_cierreDeCaja', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='casa_matriz',
            field=models.ForeignKey(to='kadoshapp.Proveedor', default=1, db_column='Casa_matriz', related_name='proveedor_casa_matriz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='empleado_recibio',
            field=models.ForeignKey(to='kadoshapp.Empleado', default=1, db_column='Empleado_recibio', related_name='empleado_empleado_recibio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_realizacion_compra',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_recepcion_compra',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_guia',
            field=models.CharField(blank=True, null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='compra',
            name='vrf_compra',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='auth_user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_baja_empleado',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fotografia_empleado',
            field=models.ImageField(upload_to='/home/developer/kadosh/sistemakadosh/archivos/', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='motivo_baja_empleado',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='producto',
            name='codigobarras_producto',
            field=models.CharField(blank=True, null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='producto',
            name='codigoestilo_producto',
            field=models.CharField(blank=True, null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(blank=True, null=True, max_length=60),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto_idtipo_producto',
            field=models.ForeignKey(to='kadoshapp.TipoProducto', default=1, db_column='Tipo_producto_idTipo_producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='casa_matrizproveedor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nit_proveedor',
            field=models.CharField(blank=True, null=True, max_length=15),
        ),
        migrations.AddField(
            model_name='venta',
            name='anotaciones_venta',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='compra',
            name='empleado_idempleado',
            field=models.ForeignKey(to='kadoshapp.Empleado', db_column='Empleado_idEmpleado', related_name='empleado_empleado_idempleado'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor_idproveedor',
            field=models.ForeignKey(to='kadoshapp.Proveedor', db_column='Proveedor_idProveedor', related_name='proveedor_proveedor_idproveedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='productohasfotografia',
            unique_together=set([]),
        ),
        migrations.DeleteModel(
            name='Combo',
        ),
        migrations.DeleteModel(
            name='DetalleInventarioRealizado',
        ),
        migrations.DeleteModel(
            name='InventarioRealizado',
        ),
        migrations.AddField(
            model_name='marcahastipoproducto',
            name='tipo_producto_idtipo_producto',
            field=models.ForeignKey(db_column='Tipo_producto_idTipo_producto', to='kadoshapp.TipoProducto'),
        ),
        migrations.AddField(
            model_name='devolucion',
            name='venta_idventa',
            field=models.ForeignKey(db_column='Venta_idVenta', to='kadoshapp.Venta'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='descuento_iddescuento',
            field=models.ForeignKey(to='kadoshapp.Descuento', default=1, db_column='Descuento_idDescuento'),
            preserve_default=False,
        ),
    ]
