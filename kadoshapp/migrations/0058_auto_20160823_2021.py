# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0057_producto_oferta_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='empleado_idempleado',
            field=models.ForeignKey(db_column='Empleado_idEmpleado', to='kadoshapp.Empleado', blank=True, null=True),
        ),
    ]
