# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0011_auto_20160712_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocionhasproducto',
            name='id',
        ),
        migrations.AddField(
            model_name='promocionhasproducto',
            name='idpromocionhasproducto',
            field=models.AutoField(serialize=False, primary_key=True, db_column='idpromocionhasproducto', default=1),
            preserve_default=False,
        ),
    ]
