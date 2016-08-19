# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0047_auto_20160818_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierredecaja',
            name='total_real_cierredecaja',
            field=models.DecimalField(db_column='total_real_cierreDeCaja', decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
    ]
