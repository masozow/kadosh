# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0002_auto_20160708_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventarioproducto',
            name='costo_unitario_inventarioproducto',
            field=models.DecimalField(blank=True, max_digits=12, null=True, decimal_places=2),
        ),
    ]
