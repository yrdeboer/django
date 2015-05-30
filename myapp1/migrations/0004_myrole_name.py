# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_myrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrole',
            name='name',
            field=models.CharField(max_length=40, default='name'),
            preserve_default=False,
        ),
    ]
