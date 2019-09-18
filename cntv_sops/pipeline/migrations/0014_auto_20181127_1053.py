# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0013_old_template_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelineinstance',
            name='name',
            field=models.CharField(default=b'default_instance', max_length=128, verbose_name='\u5b9e\u4f8b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='pipelinetemplate',
            name='name',
            field=models.CharField(default=b'default_template', max_length=128, verbose_name='\u6a21\u677f\u540d\u79f0'),
        ),
    ]
