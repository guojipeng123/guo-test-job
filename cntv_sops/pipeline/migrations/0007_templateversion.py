# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0006_auto_20180814_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('md5', models.CharField(max_length=32, verbose_name='\u5feb\u7167\u5b57\u7b26\u4e32\u7684md5')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
                ('snapshot_id', models.ForeignKey(verbose_name='\u6a21\u677f\u6570\u636e ID', to='pipeline.Snapshot')),
                ('template_id', models.ForeignKey(to='pipeline.PipelineTemplate', to_field=b'template_id', verbose_name='\u6a21\u677f ID')),
            ],
        ),
    ]
