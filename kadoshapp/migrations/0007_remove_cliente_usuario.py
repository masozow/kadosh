# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0006_remove_empleado_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
    ]
