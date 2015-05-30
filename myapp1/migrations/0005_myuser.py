# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp1', '0004_myrole_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('django_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('my_roles', models.ManyToManyField(to='myapp1.MyRole')),
            ],
        ),
    ]
