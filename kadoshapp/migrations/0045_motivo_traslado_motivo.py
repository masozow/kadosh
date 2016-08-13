# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0044_auto_20160809_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='motivo',
            name='traslado_motivo',
            field=models.BooleanField(default=True),
        ),
    ]
