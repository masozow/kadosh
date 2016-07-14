# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0012_auto_20160712_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleinventariorealizado',
            name='id',
        ),
        migrations.AddField(
            model_name='detalleinventariorealizado',
            name='iddetalleinventariorealizado',
            field=models.AutoField(serialize=False, db_column='iddetalleinventariorealizado', default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
