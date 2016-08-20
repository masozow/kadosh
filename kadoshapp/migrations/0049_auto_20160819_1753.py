# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0048_auto_20160819_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajusteinventario',
            name='cantidad_real_ajuste',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
