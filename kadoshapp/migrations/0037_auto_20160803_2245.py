# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0036_auto_20160803_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estandaresvendedor',
            old_name='ventasminimas_cliente',
            new_name='ventasminimas_vendedor',
        ),
        migrations.AlterModelTable(
            name='estandaresvendedor',
            table='Estandares_vendedor',
        ),
    ]
