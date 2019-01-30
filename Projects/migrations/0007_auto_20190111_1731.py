# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0006_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]