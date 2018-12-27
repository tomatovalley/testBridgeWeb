# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-13 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=70)),
                ('type', models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=30)),
                ('location', models.URLField(max_length=300)),
                ('device', models.CharField(choices=[('Computer', 'Computer'), ('Smartphone', 'Smartphone')], max_length=50)),
                ('features', models.CharField(max_length=400)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payPerBug', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]