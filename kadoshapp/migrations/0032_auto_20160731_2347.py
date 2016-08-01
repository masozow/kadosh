# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0031_auto_20160731_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='vendedor_venta',
            field=models.ForeignKey(related_name='empleado_empleado_vendio', db_column='vendedor_venta', to='kadoshapp.Empleado'),
        ),
    ]
