# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0052_producto_publicar_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='publicar_producto',
            field=models.BooleanField(default=False),
        ),
    ]
