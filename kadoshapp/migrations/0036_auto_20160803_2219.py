# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0035_auto_20160803_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estandarcliente',
            name='tipo_cliente_idtipo_cliente',
        ),
        migrations.RemoveField(
            model_name='estandaresvendedor',
            name='puesto_idpuesto',
        ),
        migrations.AddField(
            model_name='puesto',
            name='estandares_vendedor_idestandares_vendedor',
            field=models.ForeignKey(to='kadoshapp.EstandaresVendedor', db_column='estandares_vendedor_idestandares_vendedor', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipocliente',
            name='estandarcliente_idestandarcliente',
            field=models.ForeignKey(to='kadoshapp.EstandarCliente', db_column='estandarcliente_idestandarcliente', default=1),
            preserve_default=False,
        ),
    ]
