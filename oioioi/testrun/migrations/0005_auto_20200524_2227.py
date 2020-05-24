# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-24 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0004_auto_20200128_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testrunconfigforinstance',
            options={'verbose_name': 'test run config', 'verbose_name_plural': 'test run configs'},
        ),
        migrations.AddField(
            model_name='testrunconfigforinstance',
            name='memory_limit',
            field=models.IntegerField(null=True, verbose_name='memory limit (KiB)'),
        ),
        migrations.AddField(
            model_name='testrunconfigforinstance',
            name='time_limit',
            field=models.IntegerField(null=True, verbose_name='time limit (ms)'),
        ),
    ]
