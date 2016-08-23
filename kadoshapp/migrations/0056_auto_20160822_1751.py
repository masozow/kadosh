# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0055_auto_20160822_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='numero_factura',
            field=models.CharField(max_length=45, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='numero_invoice',
            field=models.CharField(max_length=45, blank=True, null=True),
        ),
    ]
