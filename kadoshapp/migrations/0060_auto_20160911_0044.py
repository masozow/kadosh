# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0059_auto_20160903_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiahasfotografia',
            name='vista_previa',
            field=models.BooleanField(default=False),
        ),
    ]
