# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_myuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mymodel',
            options={'permissions': (('can_view_field1', 'Can view field1'), ('can_view_field2', 'Can view field2'))},
        ),
    ]
