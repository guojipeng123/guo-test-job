# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logger_name', models.SlugField(max_length=128)),
                ('level_name', models.SlugField(max_length=32)),
                ('message', models.TextField()),
                ('exception', models.TextField()),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
                ('node_id', models.CharField(max_length=32, db_index=True)),
            ],
        ),
    ]
