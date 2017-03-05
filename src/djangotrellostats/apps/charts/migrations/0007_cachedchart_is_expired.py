# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-05 16:59
from __future__ import unicode_literals

from django.db import migrations, models


def delete_all_current_cached_charts(apps, schema):
    CachedChart = apps.get_model("charts", "CachedChart")
    CachedChart.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0006_auto_20161017_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachedchart',
            name='is_expired',
            field=models.BooleanField(default=False, verbose_name='Is this cache item expired?'),
        ),
        migrations.RunPython(delete_all_current_cached_charts)
    ]
