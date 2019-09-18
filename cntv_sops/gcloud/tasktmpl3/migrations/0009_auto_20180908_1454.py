# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def reverse_func(apps, schema_editor):
    TaskTemplate = apps.get_model('tasktmpl3', 'TaskTemplate')
    PipelineTemplate = apps.get_model('pipeline', 'PipelineTemplate')
    db_alias = schema_editor.connection.alias
    templates = TaskTemplate.objects.using(db_alias).all()
    for t in templates:
        t.pipeline_template_id = PipelineTemplate.objects.using(db_alias).get(id=t.tmp_field_id).id
        t.save()


def forward_func(apps, schema_editor):
    TaskTemplate = apps.get_model('tasktmpl3', 'TaskTemplate')
    PipelineTemplate = apps.get_model('pipeline', 'PipelineTemplate')
    db_alias = schema_editor.connection.alias
    templates = TaskTemplate.objects.using(db_alias).all()
    for t in templates:
        t.pipeline_template_id = PipelineTemplate.objects.using(db_alias).get(id=t.tmp_field_id).template_id
        t.save()


class Migration(migrations.Migration):
    dependencies = [
        ('tasktmpl3', '0008_auto_20180908_1453'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func)
    ]

