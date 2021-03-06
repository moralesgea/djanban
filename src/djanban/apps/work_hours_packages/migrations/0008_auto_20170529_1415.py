# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_hours_packages', '0007_auto_20170529_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhourspackage',
            name='offset_hours',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='This hours will be added as an initial offset of the spent time measurements gotten in the date interval', max_digits=10, verbose_name='Offset hours'),
        ),
    ]
