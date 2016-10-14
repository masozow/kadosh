# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0062_auto_20160917_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagoscuentaporcobrar',
            name='caja_idcaja',
            field=models.ForeignKey(default=1, db_column='Caja_idCaja', to='kadoshapp.Caja'),
            preserve_default=False,
        ),
    ]
