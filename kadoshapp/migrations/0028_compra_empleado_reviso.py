# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0027_auto_20160731_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='empleado_reviso',
            field=models.ForeignKey(related_name='empleado_empleado_reviso', to='kadoshapp.Empleado', db_column='Empleado_reviso', default=1),
            preserve_default=False,
        ),
    ]
