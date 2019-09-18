# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_business_life_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='always_use_executor',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u59cb\u7ec8\u4f7f\u7528\u4efb\u52a1\u6267\u884c\u8005'),
        ),
    ]
