# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0029_venta_vendedor_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='es_cotizacion',
            field=models.BooleanField(default=True),
        ),
    ]
