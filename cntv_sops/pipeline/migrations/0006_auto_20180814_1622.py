# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pipeline.models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0005_pipelineinstance_tree_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', pipeline.models.CompressJSONField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pipelineinstance',
            name='tree_info',
            field=models.ForeignKey(related_name='tree_info', verbose_name='\u63d0\u524d\u8ba1\u7b97\u597d\u7684\u4e00\u4e9b\u6d41\u7a0b\u7ed3\u6784\u6570\u636e', to='pipeline.TreeInfo', null=True),
        ),
    ]
