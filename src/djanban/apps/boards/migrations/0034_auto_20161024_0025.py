# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0033_board_is_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='type',
            field=models.CharField(choices=[('ignored', 'Ignored'), ('backlog', 'Backlog'), ('ready_to_develop', 'Ready to develop'), ('development', 'In development'), ('after_development', 'After development'), ('done', 'Done'), ('closed', 'Closed')], default='ready_to_develop', max_length=64),
        ),
    ]
