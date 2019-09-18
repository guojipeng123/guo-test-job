# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componentexecutedata',
            old_name='tag_code',
            new_name='component_code',
        ),
    ]
