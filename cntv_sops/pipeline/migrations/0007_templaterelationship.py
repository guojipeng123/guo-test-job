# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0006_auto_20180814_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ancestor_template_id', models.CharField(max_length=32, verbose_name='\u6839\u6a21\u677fID')),
                ('descendant_template_id', models.CharField(max_length=32, verbose_name='\u5b50\u6d41\u7a0b\u6a21\u677fID')),
                ('refer_sum', models.IntegerField(verbose_name='\u5f15\u7528\u6b21\u6570')),
            ],
        ),
    ]
