# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0043_auto_20171130_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
