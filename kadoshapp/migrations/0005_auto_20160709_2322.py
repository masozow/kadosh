# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0004_contacto_fecha_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cajahasempleado',
            name='id',
        ),
        migrations.AddField(
            model_name='cajahasempleado',
            name='idcaja_has_empleado',
            field=models.AutoField(serialize=False, default=1, primary_key=True, db_column='idcaja_has_empleado'),
            preserve_default=False,
        ),
    ]
