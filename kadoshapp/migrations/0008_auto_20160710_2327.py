# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0007_remove_cliente_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='descripcion_bodega',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
