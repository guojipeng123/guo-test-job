# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktmpl3', '0009_auto_20180908_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktemplate',
            name='tmp_field',
        ),
    ]
