# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-24 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pipeline.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=97, unique=True, verbose_name='\u552f\u4e00\u65b9\u6848\u540d\u79f0')),
                ('name', models.CharField(max_length=64, verbose_name='\u65b9\u6848\u540d\u79f0')),
                ('edit_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('data', pipeline.models.CompressJSONField(verbose_name='\u65b9\u6848\u6570\u636e')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pipeline.PipelineTemplate', verbose_name='\u5bf9\u5e94\u6a21\u677f ID')),
            ],
        ),
    ]