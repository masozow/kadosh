# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0042_auto_20160809_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='ventasminimas_vendedor',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True),
        ),
        migrations.AddField(
            model_name='tipocliente',
            name='comprasminimas_cliente',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=12, blank=True),
        ),
    ]
