# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0034_auto_20160801_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anaquel',
            name='bodega_idbodega',
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'managed': True, 'ordering': ['persona_idpersona']},
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'managed': True, 'ordering': ['nombres_persona', 'apellidos_persona']},
        ),
        migrations.RemoveField(
            model_name='inventarioproducto',
            name='anaquel_idanaquel',
        ),
        migrations.AddField(
            model_name='inventarioproducto',
            name='bodega_idbodega',
            field=models.ForeignKey(db_column='bodega_idbodega', default=1, to='kadoshapp.Bodega'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Anaquel',
        ),
    ]
