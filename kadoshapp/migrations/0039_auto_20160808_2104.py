# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0038_auto_20160803_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='descuento_iddescuento',
            field=models.ForeignKey(null=True, blank=True, to='kadoshapp.Descuento', db_column='Descuento_idDescuento'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='inventario_producto_idinventario_producto',
            field=models.ForeignKey(null=True, blank=True, to='kadoshapp.InventarioProducto', db_column='Inventario_producto_idInventario_producto'),
        ),
    ]
