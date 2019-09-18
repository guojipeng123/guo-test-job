# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskflow3', '0002_taskflowinstance_template_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskflowinstance',
            name='create_method',
            field=models.CharField(default=b'app', max_length=30, verbose_name='\u521b\u5efa\u65b9\u5f0f', choices=[(b'app', 'APP'), (b'api', 'API'), (b'app_maker', 'App_maker'), (b'periodic', 'Periodic_task')]),
        ),
    ]
