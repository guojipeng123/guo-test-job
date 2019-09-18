# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_environmentvariables'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='life_cycle',
            field=models.CharField(max_length=100, verbose_name='\u751f\u547d\u5468\u671f', blank=True),
        ),
    ]
