# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anaquel',
            name='codigo_anaquel',
            field=models.CharField(blank=True, unique=True, max_length=45, null=True),
        ),
    ]
