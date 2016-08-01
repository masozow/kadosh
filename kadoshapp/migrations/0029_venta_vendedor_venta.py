# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0028_compra_empleado_reviso'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='vendedor_venta',
            field=models.ForeignKey(default=1, related_name='empleado_empleado_vendio', to='kadoshapp.Empleado'),
            preserve_default=False,
        ),
    ]
