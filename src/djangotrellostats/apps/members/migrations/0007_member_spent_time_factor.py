# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20160726_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='spent_time_factor',
            field=models.DecimalField(decimal_places=2, default=1, help_text="Modify this value whe this member cost's needs to be adjusted by a factor", max_digits=5, verbose_name='Factor that needs to be multiplied on the spent time price for this member'),
        ),
    ]
