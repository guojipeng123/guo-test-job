# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0008_auto_20180824_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateversion',
            name='md5',
            field=models.CharField(max_length=32, verbose_name='\u5feb\u7167\u5b57\u7b26\u4e32\u7684md5', db_index=True),
        ),
    ]
