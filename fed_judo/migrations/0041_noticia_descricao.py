# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0040_auto_20171129_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='descricao',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
