# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import musette.models


class Migration(migrations.Migration):

    dependencies = [
        ('musette', '0007_configuration_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='favicon',
            field=models.FileField(blank=True, null=True, upload_to=musette.models.Configuration.generate_path_configuration),
        ),
        migrations.AddField(
            model_name='configuration',
            name='keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
        ),
    ]