# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def reverse_func(apps, schema_editor):
    TaskTemplate = apps.get_model('tasktmpl3', 'TaskTemplate')
    db_alias = schema_editor.connection.alias
    templates = TaskTemplate.objects.using(db_alias).all()
    for t in templates:
        t.pipeline_template_id = t.tmp_field_id
        t.tmp_field_id = None
        t.save()


def forward_func(apps, schema_editor):
    TaskTemplate = apps.get_model('tasktmpl3', 'TaskTemplate')
    db_alias = schema_editor.connection.alias
    templates = TaskTemplate.objects.using(db_alias).all()
    for t in templates:
        t.tmp_field_id = t.pipeline_template_id
        t.pipeline_template_id = None
        t.save()


class Migration(migrations.Migration):
    dependencies = [
        ('tasktmpl3', '0005_tasktemplate_tmp_field'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func)
    ]
