# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktmpl3', '0003_auto_20180301_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasktemplate',
            options={'ordering': ['-id'], 'verbose_name': '\u6d41\u7a0b\u6a21\u677f TaskTemplate', 'verbose_name_plural': '\u6d41\u7a0b\u6a21\u677f TaskTemplate', 'permissions': [('create_task', '\u65b0\u5efa\u4efb\u52a1'), ('fill_params', '\u586b\u5199\u53c2\u6570'), ('execute_task', '\u6267\u884c\u4efb\u52a1')]},
        ),
    ]
