# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadoshapp', '0022_auto_20160729_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='auth_user_id',
            new_name='auth_user',
        ),
    ]
