# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20180810_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='history_id',
            field=models.IntegerField(default=-1),
        ),
    ]
