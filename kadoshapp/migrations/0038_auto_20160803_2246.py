# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0037_auto_20160803_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='estandares_vendedor_idestandares_vendedor',
            field=models.ForeignKey(null=True, blank=True, db_column='estandares_vendedor_idestandares_vendedor', to='kadoshapp.EstandaresVendedor'),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='estandarcliente_idestandarcliente',
            field=models.ForeignKey(null=True, blank=True, db_column='estandarcliente_idestandarcliente', to='kadoshapp.EstandarCliente'),
        ),
    ]
