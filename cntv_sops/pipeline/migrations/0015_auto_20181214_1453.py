# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0014_auto_20181127_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelineinstance',
            name='execution_snapshot',
            field=models.ForeignKey(related_name='execution_snapshot_instances', verbose_name='\u7528\u4e8e\u5b9e\u4f8b\u6267\u884c\u7684\u7ed3\u6784\u6570\u636e', to='pipeline.Snapshot', null=True),
        ),
        migrations.AlterField(
            model_name='pipelineinstance',
            name='snapshot',
            field=models.ForeignKey(related_name='snapshot_instances', verbose_name='\u5b9e\u4f8b\u7ed3\u6784\u6570\u636e\uff0c\u6307\u5411\u5b9e\u4f8b\u5bf9\u5e94\u7684\u6a21\u677f\u7684\u7ed3\u6784\u6570\u636e', to='pipeline.Snapshot'),
        ),
        migrations.AlterField(
            model_name='pipelineinstance',
            name='tree_info',
            field=models.ForeignKey(related_name='tree_info_instances', verbose_name='\u63d0\u524d\u8ba1\u7b97\u597d\u7684\u4e00\u4e9b\u6d41\u7a0b\u7ed3\u6784\u6570\u636e', to='pipeline.TreeInfo', null=True),
        ),
        migrations.AlterField(
            model_name='pipelinetemplate',
            name='snapshot',
            field=models.ForeignKey(related_name='templates', verbose_name='\u6a21\u677f\u7ed3\u6784\u6570\u636e', to='pipeline.Snapshot'),
        ),
    ]
