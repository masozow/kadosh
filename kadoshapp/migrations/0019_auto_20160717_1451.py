# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0018_promocionhasproducto_cantidad_productoenpromocion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocionhasproducto',
            name='cantidad_productoenpromocion',
        ),
        migrations.AddField(
            model_name='promocionhasproducto',
            name='estado_promocion',
            field=models.BooleanField(default=True),
        ),
    ]
