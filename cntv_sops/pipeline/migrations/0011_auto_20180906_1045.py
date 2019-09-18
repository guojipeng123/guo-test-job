# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templaterelationship',
            name='refer_sum',
        ),
        migrations.AddField(
            model_name='templaterelationship',
            name='subprocess_node_id',
            field=models.CharField(default='', max_length=32, verbose_name='\u5b50\u6d41\u7a0b\u8282\u70b9 ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='templaterelationship',
            name='version',
            field=models.CharField(default='', max_length=32, verbose_name='\u5feb\u7167\u5b57\u7b26\u4e32\u7684md5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='templaterelationship',
            name='ancestor_template_id',
            field=models.CharField(max_length=32, verbose_name='\u6839\u6a21\u677fID', db_index=True),
        ),
    ]
