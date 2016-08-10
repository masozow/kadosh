# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0041_auto_20160809_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='codigo_autorización_empleado',
            new_name='codigo_autorizacion_empleado',
        ),
    ]
