# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_status_error_ignorable'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeCeleryTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_id', models.CharField(unique=True, max_length=32, verbose_name='\u8282\u70b9 ID', db_index=True)),
                ('celery_task_id', models.CharField(default=b'', max_length=40, verbose_name='celery \u4efb\u52a1 ID')),
            ],
        ),
    ]
