# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0064_venta_entregada_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='entregada_venta',
            field=models.BooleanField(default=True),
        ),
    ]
