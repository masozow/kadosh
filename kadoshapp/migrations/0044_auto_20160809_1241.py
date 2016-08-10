# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0043_auto_20160809_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puesto',
            name='estandares_vendedor_idestandares_vendedor',
        ),
        migrations.RemoveField(
            model_name='tipocliente',
            name='estandarcliente_idestandarcliente',
        ),
        migrations.DeleteModel(
            name='EstandarCliente',
        ),
        migrations.DeleteModel(
            name='EstandaresVendedor',
        ),
    ]
