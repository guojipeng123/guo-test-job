# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('periodic_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='djceleryperiodictask',
            options={'verbose_name': 'djcelery periodic task', 'verbose_name_plural': 'djcelery periodic tasks'},
        ),
    ]
