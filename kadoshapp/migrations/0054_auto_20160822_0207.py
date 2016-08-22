# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0053_auto_20160821_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='casa_matriz',
            field=models.ForeignKey(to='kadoshapp.Proveedor', related_name='proveedor_casa_matriz', db_column='Casa_matriz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='empleado_recibio',
            field=models.ForeignKey(to='kadoshapp.Empleado', related_name='empleado_empleado_recibio', db_column='Empleado_recibio', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='empleado_reviso',
            field=models.ForeignKey(to='kadoshapp.Empleado', related_name='empleado_empleado_reviso', db_column='Empleado_reviso', blank=True, null=True),
        ),
    ]
