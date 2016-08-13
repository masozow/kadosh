# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0045_motivo_traslado_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivo',
            name='traslado_motivo',
            field=models.BooleanField(),
        ),
    ]
