# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0002_auto_20180817_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componentexecutedata',
            old_name='end_time',
            new_name='archived_time',
        ),
        migrations.RenameField(
            model_name='componentexecutedata',
            old_name='elapse_time',
            new_name='elapsed_time',
        ),
        migrations.RenameField(
            model_name='componentexecutedata',
            old_name='begin_time',
            new_name='started_time',
        ),
        migrations.AddField(
            model_name='componentexecutedata',
            name='is_retry',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u91cd\u8bd5\u8bb0\u5f55'),
        ),
    ]
