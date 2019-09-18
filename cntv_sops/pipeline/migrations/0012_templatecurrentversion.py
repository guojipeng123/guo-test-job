# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0011_auto_20180906_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateCurrentVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_id', models.CharField(max_length=32, verbose_name='\u6a21\u677fID', db_index=True)),
                ('current_version', models.CharField(max_length=32, verbose_name='\u5feb\u7167\u5b57\u7b26\u4e32\u7684md5')),
            ],
        ),
    ]

