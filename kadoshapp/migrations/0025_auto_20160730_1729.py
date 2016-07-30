# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0024_auto_20160730_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='cajahasempleado',
            name='estado_asignacion_caja',
            field=models.BooleanField(db_column='estado_asignación_caja', default=True),
        ),
        migrations.AlterField(
            model_name='motivo',
            name='nombre_motivo',
            field=models.CharField(blank=True, null=True, max_length=60),
        ),
    ]
