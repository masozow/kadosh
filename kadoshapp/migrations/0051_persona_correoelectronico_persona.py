# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0050_auto_20160819_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='correoelectronico_persona',
            field=models.CharField(blank=True, null=True, max_length=60),
        ),
    ]
