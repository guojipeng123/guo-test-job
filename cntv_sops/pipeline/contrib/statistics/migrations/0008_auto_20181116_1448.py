# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0007_init_pipeline_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='atom_total',
            field=models.IntegerField(verbose_name='\u539f\u5b50\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='gateways_total',
            field=models.IntegerField(verbose_name='\u7f51\u5173\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='instance_id',
            field=models.CharField(max_length=255, verbose_name='\u5b9e\u4f8bID'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='subprocess_total',
            field=models.IntegerField(verbose_name='\u5b50\u6d41\u7a0b\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='atom_total',
            field=models.IntegerField(verbose_name='\u539f\u5b50\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='gateways_total',
            field=models.IntegerField(verbose_name='\u7f51\u5173\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='subprocess_total',
            field=models.IntegerField(verbose_name='\u5b50\u6d41\u7a0b\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='template_id',
            field=models.CharField(max_length=255, verbose_name='\u6a21\u677fID'),
        ),
    ]
