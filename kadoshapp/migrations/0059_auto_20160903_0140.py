# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0058_auto_20160823_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'managed': True, 'ordering': ['nombre_color']},
        ),
        migrations.AlterModelOptions(
            name='estilo',
            options={'managed': True, 'ordering': ['nombre_estilo']},
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'managed': True, 'ordering': ['nombre_genero']},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'managed': True, 'ordering': ['nombre_marca']},
        ),
        migrations.AlterModelOptions(
            name='talla',
            options={'managed': True, 'ordering': ['nombre_talla']},
        ),
        migrations.AlterModelOptions(
            name='tipoproducto',
            options={'managed': True, 'ordering': ['nombre_tipoproducto']},
        ),
    ]
