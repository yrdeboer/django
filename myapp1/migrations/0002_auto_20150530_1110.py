# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='field2',
            field=models.CharField(default='field 1', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default='name', max_length=40),
            preserve_default=False,
        ),
    ]
