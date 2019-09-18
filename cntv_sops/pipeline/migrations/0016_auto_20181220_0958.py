# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0015_auto_20181214_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelinetemplate',
            name='snapshot',
            field=models.ForeignKey(related_name='snapshot_templates', verbose_name='\u6a21\u677f\u7ed3\u6784\u6570\u636e', to='pipeline.Snapshot'),
        ),
    ]
