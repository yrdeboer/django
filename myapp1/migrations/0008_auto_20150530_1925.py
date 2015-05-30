# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0007_mypermissions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyPermissions',
            new_name='MyPermission',
        ),
    ]
