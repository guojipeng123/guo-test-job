# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0005_init_pipeline_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='instance_id',
            field=models.CharField(max_length=255, null=True, verbose_name='\u5b9e\u4f8bID', blank=True),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='template_id',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6a21\u677fID', blank=True),
        ),
    ]
