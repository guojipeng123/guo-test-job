# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0002_auto_20181204_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commontemplate',
            options={'ordering': ['-id'], 'verbose_name': '\u516c\u5171\u6d41\u7a0b\u6a21\u677f CommonTemplate', 'verbose_name_plural': '\u516c\u5171\u6d41\u7a0b\u6a21\u677f CommonTemplate'},
        ),
        migrations.AlterModelOptions(
            name='commontmplperm',
            options={'verbose_name': '\u516c\u5171\u6d41\u7a0b\u6a21\u677f\u6743\u9650 CommonTmplPerm', 'verbose_name_plural': '\u516c\u5171\u6d41\u7a0b\u6a21\u677f\u6743\u9650 CommonTmplPerm', 'permissions': [('common_create_task', 'common template create task'), ('common_fill_params', 'common template fill params'), ('common_execute_task', 'common template execute task')]},
        ),
    ]
