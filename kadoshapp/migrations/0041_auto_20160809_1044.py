# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0040_detalleventa_promocion_idpromocion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fotografia_empleado',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='ruta_fotografia',
            field=models.ImageField(upload_to=''),
        ),
    ]
