# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0046_auto_20160812_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='monto_gasto',
            field=models.DecimalField(default=1, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gastos',
            name='motivo_gasto',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
