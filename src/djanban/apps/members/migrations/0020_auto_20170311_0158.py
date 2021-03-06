# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-11 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_remove_member_spent_time_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trellomemberprofile',
            name='api_secret',
            field=models.CharField(blank=True, default=None, help_text='Trello API secret. Deprecated and not used. This field will be removed.', max_length=128, null=True, verbose_name='Trello API secret (obsolete)'),
        ),
    ]
