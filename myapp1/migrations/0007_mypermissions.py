# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('myapp1', '0006_auto_20150530_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPermissions',
            fields=[
                ('permission_ptr', models.OneToOneField(to='auth.Permission', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
            ],
            bases=('auth.permission',),
        ),
    ]
