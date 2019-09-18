# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pipeline.engine.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0014_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSnapshot',
            fields=[
                ('key', models.CharField(max_length=255, serialize=False, verbose_name='\u5bf9\u8c61\u552f\u4e00\u952e', primary_key=True)),
                ('obj', pipeline.engine.models.fields.IOField(verbose_name='\u5bf9\u8c61\u5b58\u50a8\u5b57\u6bb5')),
            ],
        ),
    ]
