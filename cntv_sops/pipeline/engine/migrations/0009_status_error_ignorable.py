# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_schedulecelerytask'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='error_ignorable',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u51fa\u9519\u540e\u81ea\u52a8\u5ffd\u7565'),
        ),
    ]
