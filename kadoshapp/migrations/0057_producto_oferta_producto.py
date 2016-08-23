# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0056_auto_20160822_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oferta_producto',
            field=models.BooleanField(default=False),
        ),
    ]
