# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0008_auto_20181116_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentintemplate',
            options={'verbose_name': 'Pipeline\u539f\u5b50\u88ab\u5f15\u7528\u6570\u636e', 'verbose_name_plural': 'Pipeline\u539f\u5b50\u88ab\u5f15\u7528\u6570\u636e'},
        ),
        migrations.AlterModelOptions(
            name='instanceinpipeline',
            options={'verbose_name': 'Pipeline\u5b9e\u4f8b\u5f15\u7528\u6570\u636e', 'verbose_name_plural': 'Pipeline\u5b9e\u4f8b\u5f15\u7528\u6570\u636e'},
        ),
        migrations.AlterModelOptions(
            name='templateinpipeline',
            options={'verbose_name': 'Pipeline\u6a21\u677f\u5f15\u7528\u6570\u636e', 'verbose_name_plural': 'Pipeline\u6a21\u677f\u5f15\u7528\u6570\u636e'},
        ),
    ]
