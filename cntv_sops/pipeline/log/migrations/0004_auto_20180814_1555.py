# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_logentry_history_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='exception',
            field=models.TextField(null=True, verbose_name='\u5f02\u5e38\u4fe1\u606f'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='history_id',
            field=models.IntegerField(default=-1, verbose_name='\u8282\u70b9\u6267\u884c\u5386\u53f2 ID'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='level_name',
            field=models.SlugField(max_length=32, verbose_name='\u65e5\u5fd7\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='logged_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u8f93\u51fa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='logger_name',
            field=models.SlugField(max_length=128, verbose_name='logger \u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='message',
            field=models.TextField(null=True, verbose_name='\u65e5\u5fd7\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='node_id',
            field=models.CharField(max_length=32, verbose_name='\u8282\u70b9 ID', db_index=True),
        ),
    ]
