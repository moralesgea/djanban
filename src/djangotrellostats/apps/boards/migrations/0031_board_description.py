# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-08 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0030_auto_20160925_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.TextField(blank=True, default='', max_length=128, verbose_name='Description of the board'),
        ),
    ]
