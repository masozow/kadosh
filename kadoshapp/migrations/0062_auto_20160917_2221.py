# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0061_auto_20160917_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='asunto_contacto',
            field=models.CharField(max_length=60, default=1),
            preserve_default=False,
        ),
    ]
