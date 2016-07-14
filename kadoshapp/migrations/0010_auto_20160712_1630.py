# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0009_auto_20160711_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexhasfotografia',
            name='id',
        ),
        migrations.AddField(
            model_name='indexhasfotografia',
            name='idindexhasfotografia',
            field=models.AutoField(default=1, db_column='idindexhasfotografia', serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
