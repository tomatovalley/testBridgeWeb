# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TestBridgeApp', '0007_delete_tbuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('user_type', models.CharField(max_length=30)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('creation_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('enabled', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_user',
            },
        ),
    ]
