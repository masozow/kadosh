# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0005_auto_20160709_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='usuario',
        ),
    ]
