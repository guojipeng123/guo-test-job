# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasktmpl3', '0006_auto_20180908_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktemplate',
            name='pipeline_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to_field=b'template_id', blank=True, to='pipeline.PipelineTemplate', null=True),
        ),
    ]
