# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0023_auto_20160730_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcahastipoproducto',
            name='id',
        ),
        migrations.AddField(
            model_name='marcahastipoproducto',
            name='idmarcahastipopoducto',
            field=models.AutoField(primary_key=True, default=1, db_column='idMarcaHasTipoPoducto', serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
