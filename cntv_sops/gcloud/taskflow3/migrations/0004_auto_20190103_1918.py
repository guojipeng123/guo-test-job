# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskflow3', '0003_auto_20181214_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskflowinstance',
            name='create_method',
            field=models.CharField(default=b'app', max_length=30, verbose_name='\u521b\u5efa\u65b9\u5f0f', choices=[(b'app', '\u624b\u52a8'), (b'api', 'API\u7f51\u5173'), (b'app_maker', '\u8f7b\u5e94\u7528'), (b'periodic', '\u5468\u671f\u4efb\u52a1')]),
        ),
    ]
