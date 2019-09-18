# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from pipeline.core.constants import PE


def reverse_func(apps, schema_editor):
    pass


def forward_func(apps, schema_editor):
    PipelineTemplate = apps.get_model('pipeline', 'PipelineTemplate')

    for template in PipelineTemplate.objects.all():
        if not template.is_deleted:
            acts = template.snapshot.data[PE.activities].values()
            template.has_subprocess = any([act for act in acts if act['type'] == PE.SubProcess])
            template.save()


class Migration(migrations.Migration):
    dependencies = [
        ('pipeline', '0017_pipelinetemplate_has_subprocess'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func)
    ]
