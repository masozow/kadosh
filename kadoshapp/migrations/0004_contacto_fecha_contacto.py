# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0003_inventarioproducto_costo_unitario_inventarioproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='fecha_contacto',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
