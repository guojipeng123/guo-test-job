# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0010_auto_20180830_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleservice',
            name='id',
            field=models.CharField(max_length=64, unique=True, serialize=False, verbose_name='ID \u8282\u70b9ID+version', primary_key=True),
        ),
    ]
