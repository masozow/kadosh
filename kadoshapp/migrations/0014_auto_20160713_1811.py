# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0013_auto_20160713_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleinventariorealizado',
            name='ajuste_inventario_idajuste_inventario',
            field=models.ForeignKey(db_column='Ajuste_inventario_idAjuste_inventario', null=True, to='kadoshapp.AjusteInventario'),
        ),
    ]
