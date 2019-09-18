# -*- coding: utf-8 -*-
from django.db import migrations


def set_min_template_id(apps, schema_editor):
    """
    添加用户为管理员
    """
    CommmonTemplate = apps.get_model("template", "CommonTemplate")
    CommmonTemplate.objects.create(
        id=10000,
        is_deleted=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ('template', '0003_auto_20181205_1153')
    ]
    operations = [
        migrations.RunPython(set_min_template_id)
    ]
