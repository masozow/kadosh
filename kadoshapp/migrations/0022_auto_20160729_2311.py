# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0021_auto_20160729_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marcahastipoproducto',
            old_name='marca_idmarca',
            new_name='marca_id_marca',
        ),
    ]
