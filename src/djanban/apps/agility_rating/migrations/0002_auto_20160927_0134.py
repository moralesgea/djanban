# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agility_rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectagilityrating',
            name='criticality',
            field=models.CharField(choices=[('1', 'Comfort'), ('2', 'Discretionary funds'), ('3', 'Essential funds'), ('4', 'Single life'), ('5', 'Many lives')], help_text='Consequences of a software defect.', max_length=64, verbose_name='Criticality'),
        ),
        migrations.AlterField(
            model_name='projectagilityrating',
            name='culture',
            field=models.CharField(choices=[('1', '90%'), ('2', '70%'), ('3', '50%'), ('4', '30%'), ('5', '10%')], help_text='Thriving on chaos vs. order. What percentage of tasks are disciplined done vs. on a chaotic way.', max_length=64, verbose_name='Culture'),
        ),
        migrations.AlterField(
            model_name='projectagilityrating',
            name='dynamism',
            field=models.CharField(choices=[('1', '50%'), ('2', '30%'), ('3', '10%'), ('4', '5%'), ('5', '1%')], help_text='Percentage of requirement changes per month.', max_length=64, verbose_name='Dynamism'),
        ),
        migrations.AlterField(
            model_name='projectagilityrating',
            name='personnel',
            field=models.CharField(choices=[('1', '0% Level 1B / 35% Level 2 and 3'), ('2', '10% Level 1B / 30% Level 2 and 3'), ('3', '20% Level 1B / 25% Level 2 and 3'), ('4', '30% Level 1B / 20% Level 2 and 3'), ('5', '40% Level 1B / 15% Level 2 and 3')], help_text='Personnel dimension in extended Cockburn scale.', max_length=64, verbose_name='Personnel'),
        ),
        migrations.AlterField(
            model_name='projectagilityrating',
            name='size',
            field=models.CharField(choices=[('1', '3'), ('2', '10'), ('3', '30'), ('4', '100'), ('5', '300')], help_text='Number of personnel.', max_length=64, verbose_name='Size'),
        ),
    ]
