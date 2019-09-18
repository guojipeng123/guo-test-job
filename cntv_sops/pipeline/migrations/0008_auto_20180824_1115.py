# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0007_templateversion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templateversion',
            old_name='snapshot_id',
            new_name='snapshot',
        ),
        migrations.RemoveField(
            model_name='templateversion',
            name='template_id',
        ),
        migrations.AddField(
            model_name='templateversion',
            name='template',
            field=models.ForeignKey(default='', verbose_name='\u6a21\u677f ID', to='pipeline.PipelineTemplate'),
            preserve_default=False,
        ),
    ]
