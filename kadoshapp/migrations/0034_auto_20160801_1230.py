# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0033_auto_20160801_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='marca_idmarca',
            new_name='marca_id_marca',
        ),
    ]
