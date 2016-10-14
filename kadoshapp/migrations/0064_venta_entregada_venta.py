# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0063_pagoscuentaporcobrar_caja_idcaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='entregada_venta',
            field=models.BooleanField(default=False),
        ),
    ]
