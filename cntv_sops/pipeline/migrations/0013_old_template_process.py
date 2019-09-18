# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.db.models.signals import post_save


def reverse_func(apps, schema_editor):
    pass


def forward_func(apps, schema_editor):
    PipelineTemplate = apps.get_model('pipeline', 'PipelineTemplate')
    TemplateRelationship = apps.get_model('pipeline', 'TemplateRelationship')
    TemplateVersion = apps.get_model('pipeline', 'TemplateVersion')
    TemplateCurrentVersion = apps.get_model('pipeline', 'TemplateCurrentVersion')
    db_alias = schema_editor.connection.alias
    template_list = PipelineTemplate.objects.using(db_alias).filter(is_deleted=False)
    
    for template in template_list:
        TemplateRelationship.objects.using(db_alias).filter(ancestor_template_id=template.template_id).delete()
        acts = template.snapshot.data['activities'].values()
        subprocess_nodes = [act for act in acts if act["type"] == 'SubProcess']
        rs = []
        for sp in subprocess_nodes:
            version = sp.get('version') or PipelineTemplate.objects\
                                                           .using(db_alias)\
                                                           .get(template_id=sp['template_id'])\
                                                           .snapshot\
                                                           .md5sum
            rs.append(TemplateRelationship(ancestor_template_id=template.template_id,
                                           descendant_template_id=sp['template_id'],
                                           subprocess_node_id=sp['id'][:32],
                                           version=version))
        TemplateRelationship.objects.bulk_create(rs)

        versions = TemplateVersion.objects.using(db_alias).filter(template_id=template.id).order_by('-id')
        if not (versions and versions[0].md5 == template.snapshot.md5sum):
            TemplateVersion.objects.create(template=template, snapshot=template.snapshot, md5=template.snapshot.md5sum)
        TemplateCurrentVersion.objects.update_or_create(template_id=template.template_id,
                                                        defaults={
                                                            'current_version': template.snapshot.md5sum
                                                        })


class Migration(migrations.Migration):
    dependencies = [
        ('pipeline', '0012_templatecurrentversion'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func)
    ]
