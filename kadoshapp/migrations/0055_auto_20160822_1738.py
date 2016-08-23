# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0054_auto_20160822_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='nombre_color',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estilo',
            name='nombre_estilo',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genero',
            name='nombre_genero',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombre_marca',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talla',
            name='nombre_talla',
            field=models.CharField(default=1, db_column='nombre_Talla', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='nombre_tipoproducto',
            field=models.CharField(default=1, db_column='nombre_tipoProducto', max_length=50),
            preserve_default=False,
        ),
    ]
