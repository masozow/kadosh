# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0010_auto_20160712_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticiahasfotografia',
            name='id',
        ),
        migrations.AddField(
            model_name='noticiahasfotografia',
            name='idnoticiahasfotografia',
            field=models.AutoField(serialize=False, db_column='idnoticiahasfotografia', primary_key=True, default=1),
            preserve_default=False,
        ),
    ]
