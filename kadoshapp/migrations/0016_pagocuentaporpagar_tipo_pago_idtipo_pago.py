# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0015_auto_20160713_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagocuentaporpagar',
            name='tipo_pago_idtipo_pago',
            field=models.ForeignKey(db_column='Tipo_pago_idTipo_pago', to='kadoshapp.TipoPago', default=1),
            preserve_default=False,
        ),
    ]
