# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0016_pagocuentaporpagar_tipo_pago_idtipo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='fechainicial_precio',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, db_column='fechaInicial_precio'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_inicialpromocion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, db_column='fecha_inicialPromocion'),
        ),
    ]
