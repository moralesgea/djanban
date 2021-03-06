# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 18:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0023_auto_20170519_1715'),
        ('boards', '0071_auto_20170530_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurrentCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='Recurrent card name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description of the card')),
                ('position', models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom')], default='top', max_length=8, verbose_name='Position in the list')),
                ('estimated_time', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True, verbose_name='Estimated time of this recurrent card')),
                ('is_active', models.BooleanField(default=False, verbose_name='Should this cards be created?')),
            ],
            options={
                'verbose_name': 'recurrent card',
                'verbose_name_plural': 'recurrent cards',
            },
        ),
        migrations.CreateModel(
            name='WeeklyRecurrentCard',
            fields=[
                ('recurrentcard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='recurrent_cards.RecurrentCard')),
                ('create_on_mondays', models.BooleanField(default=False, verbose_name='Creation on mondays')),
                ('create_on_tuesdays', models.BooleanField(default=False, verbose_name='Creation on tuesdays')),
                ('create_on_wednesdays', models.BooleanField(default=False, verbose_name='Creation on wednesdays')),
                ('create_on_thursdays', models.BooleanField(default=False, verbose_name='Creation on thursdays')),
                ('create_on_fridays', models.BooleanField(default=False, verbose_name='Creation on fridays')),
                ('create_on_saturdays', models.BooleanField(default=False, verbose_name='Creation on saturdays')),
                ('create_on_sundays', models.BooleanField(default=False, verbose_name='Creation on sundays')),
                ('deadline', models.DurationField(blank=True, default=datetime.timedelta(1), help_text='Default deadline of the card from the creation datetime of it (00:00:00 hours of each day)', null=True, verbose_name='Deadline of the card')),
                ('move_on_deadline_to_list', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moved_recurrent_cards', to='boards.List', verbose_name='Automatically move the card to this list when reaching deadline')),
            ],
            bases=('recurrent_cards.recurrentcard',),
        ),
        migrations.AddField(
            model_name='recurrentcard',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurrent_cards', to='boards.Board', verbose_name='Recurrent cards'),
        ),
        migrations.AddField(
            model_name='recurrentcard',
            name='creation_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurrent_cards', to='boards.List', verbose_name='Creation list for the recurrent cards'),
        ),
        migrations.AddField(
            model_name='recurrentcard',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_recurrent_cards', to='members.Member', verbose_name='Created recurrent cards'),
        ),
        migrations.AddField(
            model_name='recurrentcard',
            name='labels',
            field=models.ManyToManyField(related_name='recurrent_cards', to='boards.Label'),
        ),
        migrations.AddField(
            model_name='recurrentcard',
            name='members',
            field=models.ManyToManyField(related_name='recurrent_cards', to='members.Member', verbose_name='Members'),
        ),
    ]
