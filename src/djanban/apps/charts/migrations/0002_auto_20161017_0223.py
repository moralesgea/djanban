# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartcache',
            name='board',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chart_caches', to='boards.Board', verbose_name='Board'),
        ),
    ]
