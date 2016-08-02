# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0032_auto_20160731_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcahastipoproducto',
            name='marca_id_marca',
        ),
        migrations.RemoveField(
            model_name='marcahastipoproducto',
            name='tipo_producto_idtipo_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='marca_idmarca',
            field=models.ForeignKey(default=1, to='kadoshapp.Marca', db_column='marca_idmarca'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MarcaHasTipoProducto',
        ),
    ]
