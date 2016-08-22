# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0051_persona_correoelectronico_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='publicar_producto',
            field=models.BooleanField(default=True),
        ),
    ]
