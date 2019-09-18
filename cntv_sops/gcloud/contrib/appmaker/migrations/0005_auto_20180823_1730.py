# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmaker', '0004_auto_20180425_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appmaker',
            old_name='template_schema_id',
            new_name='template_scheme_id',
        ),
    ]
