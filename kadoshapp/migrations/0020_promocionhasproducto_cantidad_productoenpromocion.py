# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0019_auto_20160717_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocionhasproducto',
            name='cantidad_productoenpromocion',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
