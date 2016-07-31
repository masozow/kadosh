# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0026_auto_20160731_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_realizacion_compra',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_recepcion_compra',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
