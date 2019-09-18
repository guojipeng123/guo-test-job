# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0013_old_template_process'),
        ('tasktmpl3', '0004_auto_20180822_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktemplate',
            name='tmp_field',
            field=models.ForeignKey(related_name='tmp_field_id', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pipeline.PipelineTemplate', null=True),
        ),
    ]
