# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskflow3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskflowinstance',
            name='template_source',
            field=models.CharField(default=b'business', max_length=32, verbose_name='\u6d41\u7a0b\u6a21\u677f\u6765\u6e90', choices=[(b'business', '\u4e1a\u52a1\u6d41\u7a0b'), (b'common', '\u516c\u5171\u6d41\u7a0b')]),
        ),
    ]
