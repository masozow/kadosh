# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0039_auto_20160808_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='promocion_idpromocion',
            field=models.ForeignKey(null=True, db_column='Promocion_idPromocion', blank=True, to='kadoshapp.Promocion'),
        ),
    ]
