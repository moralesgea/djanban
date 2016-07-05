# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the board')),
                ('uuid', models.CharField(max_length=128, unique=True, verbose_name='Trello id of the board')),
                ('last_activity_date', models.DateTimeField(default=None, null=True, verbose_name='Last activity date')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='members.Member', verbose_name='Member')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the card')),
                ('uuid', models.CharField(max_length=128, verbose_name='Trello id of the card')),
                ('url', models.CharField(max_length=128, verbose_name='URL of the card')),
                ('short_url', models.CharField(max_length=128, verbose_name='Short URL of the card')),
                ('description', models.TextField(verbose_name='Description of the card')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Is this card closed?')),
                ('position', models.PositiveIntegerField(verbose_name='Position in the list')),
                ('last_activity_date', models.DateTimeField(verbose_name='Last activity date')),
                ('spent_time', models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Actual card spent time')),
                ('estimated_time', models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Estimated card completion time')),
                ('cycle_time', models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Lead time')),
                ('lead_time', models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Cycle time')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='boards.Board', verbose_name='Board')),
            ],
        ),
        migrations.CreateModel(
            name='Fetch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(verbose_name='Date this object was created')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fetches', to='boards.Board', verbose_name='Board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the label')),
                ('uuid', models.CharField(max_length=128, unique=True, verbose_name='Trello id of the label')),
                ('color', models.CharField(max_length=128, verbose_name='Color of the label')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='boards.Board', verbose_name='Board')),
                ('fetch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='boards.Fetch', verbose_name='Fetch')),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the board')),
                ('uuid', models.CharField(max_length=128, unique=True, verbose_name='Trello id of the list')),
                ('type', models.CharField(choices=[('normal', 'Normal'), ('development', 'In development'), ('done', 'Done')], default='normal', max_length=64)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='boards.Board', verbose_name='Board')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of the workflow')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflows', to='boards.Board', verbose_name='Workflow')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(verbose_name='Order of the list')),
                ('is_done_list', models.BooleanField(default=False, verbose_name='Informs if the list is a done list')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflowlist', to='boards.List', verbose_name='List')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflowlists', to='boards.Workflow', verbose_name='Workflow')),
            ],
        ),
        migrations.AddField(
            model_name='workflow',
            name='lists',
            field=models.ManyToManyField(related_name='workflow', through='boards.WorkflowList', to='boards.List'),
        ),
        migrations.AddField(
            model_name='card',
            name='fetch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='boards.Fetch', verbose_name='Fetch'),
        ),
        migrations.AddField(
            model_name='card',
            name='labels',
            field=models.ManyToManyField(related_name='cards', to='boards.Label'),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='boards.List', verbose_name='List'),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together=set([('uuid', 'fetch')]),
        ),
        migrations.AlterUniqueTogether(
            name='card',
            unique_together=set([('uuid', 'fetch')]),
        ),
    ]
