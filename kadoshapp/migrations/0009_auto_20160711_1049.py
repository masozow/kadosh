# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0008_auto_20160710_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productohasfotografia',
            name='id',
        ),
        migrations.AddField(
            model_name='productohasfotografia',
            name='idproductohasfotografia',
            field=models.AutoField(default=1, primary_key=True, serialize=False, db_column='idproductohasfotografia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='nombre_fotografia',
            field=models.CharField(default='s/n', null=True, max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='ruta_fotografia',
            field=models.ImageField(upload_to='/home/developer/kadosh/sistemakadosh/archivos/'),
        ),
        migrations.AlterField(
            model_name='talla',
            name='idtalla',
            field=models.AutoField(primary_key=True, serialize=False, db_column='idTalla'),
        ),
    ]
