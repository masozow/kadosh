# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0060_auto_20160911_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo_contacto',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
