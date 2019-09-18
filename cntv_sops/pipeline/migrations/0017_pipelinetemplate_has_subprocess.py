# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0016_auto_20181220_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipelinetemplate',
            name='has_subprocess',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u542b\u6709\u5b50\u6d41\u7a0b'),
        ),
    ]
