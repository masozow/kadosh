# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0049_auto_20160819_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajusteinventario',
            name='empleado_idempleado',
            field=models.ForeignKey(null=True, db_column='Empleado_idEmpleado', to='kadoshapp.Empleado', blank=True),
        ),
    ]
