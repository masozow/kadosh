# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0025_auto_20160730_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='casa_matriz',
            field=models.ForeignKey(to='kadoshapp.Proveedor', db_column='Casa_matriz', blank=True, related_name='proveedor_casa_matriz'),
        ),
    ]
