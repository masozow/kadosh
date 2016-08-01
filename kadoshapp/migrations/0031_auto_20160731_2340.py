# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0030_venta_es_cotizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='es_cotizacion',
            field=models.BooleanField(default=False),
        ),
    ]
